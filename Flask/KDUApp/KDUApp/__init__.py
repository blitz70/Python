from flask import Flask, render_template, flash, request, url_for, redirect, session
#from wtforms import Form, validators, BooleanField, StringField, PasswordField
#from passlib.hash import sha256_crypt as en
from pymysql import escape_string as es
import gc

from functools import wraps
#from .survey_content import questions


app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)


root_path = ''
survey_result = {}
survey_result2 = []


@app.route('/')
def homepage():
    return render_template('home.html', root_path=root_path)

@app.route('/survey_industry/')
def survey_industry():
    return render_template('survey_industry.html', root_path=root_path)

@app.route('/survey_start/', methods=['GET', 'POST'])
def survey_start():
    if request.method == 'POST':
        for item in request.form:
            if item == 'submit':
                continue
            survey_result[item] = request.form[item]
            survey_result2.append([item, request.form[item]])
        # return redirect(url_for('survey_done'))
        return redirect("http://inhappy.kr/mc/?id=KDUBMLS")
    return render_template('survey_start.html', root_path=root_path)


@app.route('/survey_end/')
def survey_done():
    return render_template('survey_done.html', survey_result=survey_result, survey_result2=survey_result2, root_path=root_path)

if __name__ == "__main__":
    app.run()
