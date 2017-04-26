from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello Python3 Flask on AWS! by BLITZ"


if __name__ == "__main__":
    app.run()
