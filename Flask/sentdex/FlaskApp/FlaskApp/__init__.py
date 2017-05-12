from flask import Flask, render_template, flash, request, url_for, redirect, session

from wtforms import Form, validators, BooleanField, StringField, PasswordField
from passlib.hash import sha256_crypt as en
from pymysql import escape_string as es
import gc

from functools import wraps

from .content_management import Content
from .db_connect import connect

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)

topics_dict = Content()
root_path = '/FlaskTutorials'


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
                return redirect(url_for('pp1'))
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
    return render_template('error.html', error=error, error_msg="Opps that page doesn't exist. [404]", root_path=root_path)


@app.errorhandler(405)
def error_405(error):
    return render_template('error.html', error=error, error_msg="Wrong method mate. [405]", root_path=root_path)


@app.errorhandler(500)
def error_500(error):
    return render_template('error.html', error=error, error_msg="Server is confused right now. [500]", root_path=root_path)


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


@app.route('/introduction-to-python-programming/')
def pp1():
    return '''
    <h1>Welcome!</h1>
    <a href='FlaskTutorials/'>Back to home</a>'''


@app.route('/include_page/')
def include_page():
    replies = {'Jack': 'Cool post',
               'Jane': '+1',
               'Erika': 'Most definitely',
               'Bob': 'wow',
               'Carl': 'amazing!',}
    return render_template('include_page.html', replies=replies, root_path=root_path)


if __name__ == "__main__":
    app.run()
