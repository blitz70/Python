from flask import Flask, render_template
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

if __name__ == "__main__":
    app.run()
