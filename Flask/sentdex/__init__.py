from flask import Flask, render_template

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD = True)

@app.route('/')
def homepage():
    return render_template('main.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run()
