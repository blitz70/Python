from flask import Flask, render_template, flash
from .content_management import content

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD = True)

@app.route('/')
def homepage():
    return render_template('main.html')

@app.route('/dashboard/')
def dashboard():
    topics_dict = content()
    return render_template('dashboard.html', topics_dict = topics_dict)

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

@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')



if __name__ == "__main__":
    app.run()
