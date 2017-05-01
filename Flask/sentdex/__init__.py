from flask import Flask, render_template, flash, request, url_for, redirect, session

from wtforms import Form, validators, BooleanField, StringField, PasswordField
from passlib.hash import sha256_crypt
from pymysql import escape_string
import gc

from .content_management import content
from .db_connect import connect

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)


@app.route('/')
def homepage():
    return render_template('main.html')


@app.route('/dashboard/')
def dashboard():
    topics_dict = content()
    return render_template('dashboard.html', topics_dict=topics_dict)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            user_name = request.form['username']
            user_password = request.form['userpassword']
            if user_name == 'admin' and user_password == 'pass':
                flash(' '.join(['N:', str(user_name), ', P:', str(user_password)]))
                return redirect(url_for('dashboard'))
            else:
                flash(' '.join(['N:', str(user_name), ', P:', str(user_password)]))
                return render_template('login.html', error='Wrong credentials, try again.')
        else:
            return render_template('login.html')
    except Exception as e:
        return render_template('login.html', error=e)


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
            user_name = escape_string(form.user_name.data)
            user_email = escape_string(form.user_email.data)
            user_password = sha256_crypt.encrypt(escape_string(form.user_password.data))
            c, conn = connect()
            sql = c.execute("SELECT * FROM users WHERE username = '{}'".format(user_name))
            if sql > 0:  # user exits
                flash('That username is taken, choose another please.')
                return render_template('register.html', form=form)
            else:  # register user
                c.execute("INSERT INTO users (username, password, email, tracking) VALUES ('{0}', '{1}', '{2}', '{3}')".
                    format(user_name, user_password, user_email, '/introduction-to-python-programming/'))
                conn.commit()
                c.close()
                conn.close()
                gc.collect()
                flash('Thank you for joining, enjoy!')
                session['logged'] = True
                session['user'] = user_name
                return redirect(url_for('pp1'))
        return render_template('register.html', form=form)
    except Exception as e:
        flash(' '.join(['Registration error : ', str(e)]))
        return render_template('register.html', form=form)










@app.errorhandler(404)
def error_404(error):
    return render_template('error.html', error=error, error_msg="Opps that page doesn't exist. [404]")


@app.errorhandler(405)
def error_405(error):
    return render_template('error.html', error=error, error_msg="Wrong method mate. [405]")


@app.errorhandler(500)
def error_500(error):
    return render_template('error.html', error=error, error_msg="Server is confused right now. [500]")


@app.route('/flashboard/')
def flashboard():
    flash('This is the')
    flash('2nd line of')
    flash('flash messages!!')
    return render_template('flashboard.html')


@app.route('/jumped/')
def landed():
    return 'I jumped!'


@app.route('/jump/')
def jump_page():
    return redirect(url_for('landed'))


@app.route('/introduction-to-python-programming/')
def pp1():
    return 'introduction-to-python-programming'

if __name__ == "__main__":
    app.run()
