from flask import Flask, render_template, flash, request, url_for, redirect, session
#from wtforms import Form, validators, BooleanField, StringField, PasswordField
#from passlib.hash import sha256_crypt as en
from pymysql import escape_string as es
import gc

from functools import wraps
from .survey_content import questions


app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)


root_path = ''
survey_result = {}
survey_content = []


@app.route('/')
def homepage():
    return render_template('home.html', root_path=root_path)


@app.route('/survey_industry/', methods=['GET', 'POST'])
def industry_survey():
    if request.method == 'POST':
        for item in request.form:
            if item == 'submit':
                continue
            survey_result[item] = request.form[item]
        return redirect(url_for('survey_done'))
    return render_template('survey_industry.html', questions=questions(), root_path=root_path)


@app.route('/survey_done/')
def survey_done():
    return render_template('survey_done.html', survey_result=survey_result, root_path=root_path)

if __name__ == "__main__":
    app.run()
