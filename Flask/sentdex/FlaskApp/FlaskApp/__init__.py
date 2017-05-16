from flask import Flask, render_template, request, url_for, redirect, session
from flask import flash, send_file, send_from_directory, jsonify

from wtforms import Form, validators, BooleanField, StringField, PasswordField
from passlib.hash import sha256_crypt as en
from pymysql import escape_string as es
from functools import wraps

import gc
from flask_mail import Mail, Message
import pygal

from .content_management import Content
from .my_security import connect, mail_info

topics_dict = Content()
root_path = '/FlaskTutorials'
info_mail = mail_info()

app = Flask(__name__)
app.config.update(
    TEMPLATES_AUTO_RELOAD=True,
    # Email settings
    MAIL_SERVER=info_mail[0],
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=info_mail[1],
    MAIL_PASSWORD=info_mail[2]
)
mail = Mail(app)


# @app.route('/<path:urlpath>/')
# def homepage(urlpath='/'):
@app.route('/')
def homepage():
    try:
        if session['logged'] is None:
            session['user'] = False
            session['logged'] = False
    except:
        pass
    return render_template('home.html', root_path=root_path)


@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html', topics_dict=topics_dict, root_path=root_path)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            user_name = es(request.form['username'])
            user_password = es(request.form['userpassword'])
            c, conn = connect()
            data_e = c.execute("SELECT * FROM users WHERE username = (%s)", (user_name, ))
            data_f = c.fetchone()
            c.close()
            conn.close()
            gc.collect()
            if data_e > 0:
                if en.verify(user_password, data_f[2]):
                    session['logged'] = True
                    session['user'] = user_name
                    flash(''.join(['Welcome back ', str(user_name), '!']))
                    # return redirect(str(data_f[5]))
                    return redirect(url_for('dashboard'))
            flash('Wrong credentials, try again please.')
        return render_template('login.html', root_path=root_path)
    except Exception as e:
        flash(' '.join(['Login error : ', str(e)]))
        return render_template('login.html', root_path=root_path)


class RegisterForm(Form):
    user_name = StringField('User name', [validators.Length(min=4, max=20)])
    user_email = StringField('User email', [validators.Length(min=6, max=50)])
    user_password = PasswordField('User password',
                                  [validators.DataRequired(),
                                   validators.EqualTo('confirm_password', message='Password must match.')])
    confirm_password = PasswordField('Repeat password')
    accept_tos = BooleanField('''
        Accept <a href="/tos/">Terms of Service</a> and <a href="/pn/">Privacy Notice</a>.
        ''', [validators.DataRequired()])


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    try:
        if request.method == 'POST' and form.validate():
            user_name = es(form.user_name.data)
            user_email = es(form.user_email.data)
            user_password = en.encrypt(es(form.user_password.data))
            c, conn = connect()
            # sql = c.execute("SELECT * FROM users WHERE username = '{}'".format(user_name))
            sql = c.execute("SELECT * FROM users WHERE username = %s", (user_name, ))
            if sql > 0:  # user exits
                flash('That username is taken, choose another please.')
                return render_template('register.html', form=form)
            else:  # register user
                # c.execute("INSERT INTO users (username, password, email, tracking) VALUES ('{0}', '{1}', '{2}', '{3}')".
                #    format(user_name, user_password, user_email, '/introduction-to-python-programming/'))
                c.execute("INSERT INTO users (username, password, email, tracking) VALUES (%s, %s, %s, %s)",
                          (user_name, user_password, user_email, '/introduction-to-python-programming/'))
                conn.commit()
                c.close()
                conn.close()
                gc.collect()
                session['logged'] = True
                session['user'] = user_name
                flash('Thank you for joining, enjoy!')
                msg = Message("New user joined",
                              sender="blitz70@hanmail.net",
                              recipients=["blitz70@hanmail.net"])
                msg.body = "User: " + user_name
                msg.html = render_template('join_mail.html', user=[user_name, user_password, user_email])
                mail.send(msg)
                return redirect(url_for('private'))
        return render_template('register.html', form=form, root_path=root_path)
    except Exception as e:
        flash(' '.join(['Registration error : ', str(e)]))
        return render_template('register.html', form=form, root_path=root_path)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['logged'] is True:
            return f(*args, **kwargs)
        else:
            flash('Members only, login please')
            return redirect(url_for('login'))
    return wrap


@app.route('/private/')
@login_required
def private():
    return render_template('private.html', user=session['user'], root_path=root_path)


@app.route('/logout/')
@login_required
def logout():
    flash(''.join(['Goodbye ', session['user']]))
    session['user'] = False
    session['logged'] = False
    gc.collect()
    return redirect(url_for('homepage'))


@app.errorhandler(404)
def error_404(error):
    return render_template('error.html', error=error, error_msg="What page? [404]", root_path=root_path)


@app.errorhandler(405)
def error_405(error):
    return render_template('error.html', error=error, error_msg="Wrong method mate. [405]", root_path=root_path)


@app.errorhandler(500)
def error_500(error):
    return render_template('error.html', error=error, error_msg="I'm confused. [500]", root_path=root_path)


@app.route('/flashboard/')
def flashboard():
    flash('This is the')
    flash('2nd line of')
    flash('flash messages!!')
    return render_template('flashboard.html', root_path=root_path)


@app.route('/jumped/')
def landed():
    return 'I jumped!'


@app.route('/jump/')
def jump_page():
    return redirect(url_for('landed'))


@app.route('/part2/')
def part2():
    return render_template('part2/part2.html', root_path=root_path)


@app.route('/includes/')
def include():
    replies = {'Jack': 'Cool post',
               'Jane': '+1',
               'Erika': 'Most definitely',
               'Bob': 'wow',
               'Carl': 'amazing!', }
    return render_template('part2/includes.html', replies=replies, root_path=root_path)


@app.route('/jinja/')
def jinja():
    data = [15, '15', 'Python is good', 'Python, Java, PHP, SQL, C++', '<p><strong>Hey There!</strong></p>']
    return render_template('part2/jinja.html', data=data, root_path=root_path)


@app.route('/converters1/')
@app.route('/converters1/<int:page>/')
def converters1(page=1):
    return render_template('part2/converters.html', page=page, root_path=root_path)


@app.route('/converters2/')
@app.route('/converters2/<path:urlpath>/')
def converters2(urlpath='this/is/a/directory'):
    return render_template('part2/converters.html', urlpath=urlpath, root_path=root_path)


@app.route('/converters3/')
@app.route('/converters3/<string:article>/<int:page>/')
def converters3(article='chapter1', page=1):
    return render_template('part2/converters.html', article=article, page=page, root_path=root_path)


@app.route('/send_mail/')
def send_mail():
    try:
        msg = Message("flask mail title",
                      sender="blitz70@hanmail.net",
                      recipients=["blitz70@hanmail.net"])
        msg.body = "flask mail content"
        mail.send(msg)
        return 'Mail sent'
    except Exception as e:
        flash(str(e))
        return redirect(url_for('homepage'))


@app.route("/file_send/")
def file_send():
    try:
        return send_file('/var/www/FlaskApp/FlaskApp/static/images/python-programming-tutorials-main.png')
    except Exception as e:
        flash(str(e))
        return redirect(url_for('homepage'))


def secret(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            if session['user'] == 'blitz':
                return f(*args, **kwargs)
        except:
            flash("Try again")
            return redirect(url_for('homepage'))
    return wrap


@app.route("/protected/")
@secret
def protected():
    try:
        return send_from_directory("/var/www/FlaskApp/FlaskApp/protected/", "secret.jpg")
    except Exception as e:
        flash(str(e))
        return redirect(url_for("homepage"))


@app.route('/interactive/')
def interactive():
    return render_template('part2/interactive.html', root_path=root_path)


@app.route('/_background_process/')
def _background_process():
    try:
        proglang = request.args.get('proglang')
        if 'python' in str(proglang).lower():
            return jsonify(answer='You are wise!(server)')
        else:
            return jsonify(answer='Try again (server)')
    except Exception as e:
        flash(str(e))
        return redirect(url_for('homepage'))


@app.route('/graph/')
def graph():
    _charts = [pygal.Line(), pygal.Bar(), pygal.Histogram(), pygal.XY(), pygal.Pie(), pygal.Radar(), pygal.Box(),
               pygal.Dot(), pygal.Funnel(), pygal.SolidGauge(), pygal.Gauge(), pygal.Pyramid(), pygal.Treemap()]
    charts = []
    for chart in _charts:
        chart.title = '% Change Coolness of programming languages over time.'
        chart.x_labels = ['2011', '2012', '2013', '2014', '2015', '2016']
        chart.add('Python', [15, 31, 89, 200, 356, 900])
        chart.add('Java', [15, 45, 76, 80, 91, 95])
        chart.add('C++', [5, 51, 54, 102, 150, 201])
        chart.add('All others combined!', [5, 15, 21, 55, 92, 105])
        charts.append(chart.render_data_uri())
    return render_template('part2/graph.html', charts=charts, root_path=root_path)


if __name__ == "__main__":
    app.run()
