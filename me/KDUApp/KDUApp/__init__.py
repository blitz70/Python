from flask import Flask, render_template, request, url_for, redirect
import gc
import json

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
        results = []
        for item in request.form:
            if item == 'submit':
                continue
            results.append([item, request.form[item]])
        results.sort(key=lambda x: x[0])
        save_data(results, '/var/www/KDUApp/KDUApp/data/results.txt')
        # return render_template('survey_results.html', results=results_l, root_path=root_path)
        return redirect("http://inhappy.kr/mc/?id=KDUBMLS")
    return render_template('survey_start.html', root_path=root_path)


@app.route('/survey_results/')
def survey_results():
    results = load_data('/var/www/KDUApp/KDUApp/data/results.txt')
    return render_template('survey_results.html', results=results, root_path=root_path)


def save_data(data, file):
    try:
        with open(file, 'a') as f:
            json_txt = json.dumps(data)
            f.write(json_txt + '\n')
    except Exception as e:
        print(e)
    gc.collect()


def load_data(file):
    try:
        data = []
        with open(file, 'r') as f:
            for line in f.readlines():
                data.append(json.loads(line))
        return data
    except Exception as e:
        print(e)
    gc.collect()

if __name__ == "__main__":
    app.run()
