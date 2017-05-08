from flask import Flask, render_template, request, url_for, redirect
import gc


app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)


root_path = ''

@app.route('/')
def homepage():
    return render_template('home.html', root_path=root_path)

@app.route('/survey_industry/')
def survey_industry():
    return render_template('survey_industry.html', root_path=root_path)

@app.route('/survey_start/', methods=['GET', 'POST'])
def survey_start():
    if request.method == 'POST':
        results_l = []
        for item in request.form:
            if item == 'submit':
                continue
            results_l.append([item, request.form[item]])
        save_data(results_l)
        # return render_template('survey_done.html', results=results_l, root_path=root_path)
        return redirect("http://inhappy.kr/mc/?id=KDUBMLS")
    return render_template('survey_start.html', root_path=root_path)


def save_data(data):
    data_str = str(str(data).encode('utf-8'))
    try:
        with open('/var/www/KDUApp/KDUApp/data/results.txt', 'a') as f:
            f.write(data_str + '\n')
    except:
        pass
    gc.collect()


@app.route('/survey_end/')
def survey_done():
    return render_template('survey_done.html', results=results_l, root_path=root_path)

if __name__ == "__main__":
    app.run()
