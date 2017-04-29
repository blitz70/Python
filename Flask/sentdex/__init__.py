from flask import Flask, render_template, flash, request, url_for, redirect
from .content_management import content
from .db_connect import connect

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD = True)

@app.route('/')
def homepage():
    return render_template('main.html')

@app.route('/dashboard/')
def dashboard():
    topics_dict = content()
    return render_template('dashboard.html', topics_dict = topics_dict)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            user = request.form['username']
            pwd = request.form['password']
            if user == 'admin' and pwd == 'pass':
                flash(' '.join(['Username:', str(user), ', Password:', str(pwd)]))
                return redirect(url_for('dashboard'))
            else:
                flash(' '.join(['Username:', str(user), ', Password:', str(pwd)]))
                return render_template('login.html', error = 'Wrong credentials, try again.')
        else:
            return render_template('login.html')
    except Exception as e:
        return render_template('login.html', error = e)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    try:
        c, conn = connect()
        return render_template('register.html', msg = 'Success !')
    except Exception as e:
        return render_template('register.html', msg = 'Fail !', error = e)










@app.errorhandler(404)
def error_404(error):
    return render_template('error.html', error = error, error_msg = "Opps that page doesn't exist. [404]")

@app.errorhandler(405)
def error_405(error):
    return render_template('error.html', error = error, error_msg = "Wrong method mate. [405]")

@app.errorhandler(500)
def error_500(error):
    return render_template('error.html', error = error, error_msg = "Server is confused right now. [500]")

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

if __name__ == "__main__":
    app.run()
