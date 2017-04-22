from flask import Flask, request, render_template

app = Flask(__name__)

# routing
@app.route('/')
def index():
    return 'This is index page'

@app.route('/author')
def author():
    return '<h2>Blitz love Python!</h2>'

# passing variables
@app.route('/profile/<user_name>')
def profile(user_name):
    print(type(user_name))
    return "This is <strong>%s</strong>'s page" % user_name

@app.route('/post/<int:post_id>')
def post(post_id):
    print(type(post_id))
    return "This is the contend of post {}".format(post_id)

# HTTP methods
@app.route('/get')
def get():
    return 'This page request method is [{}]'.format(request.method)

@app.route('/methods', methods=['GET', 'POST'])
def methods():
    if request.method == 'POST':
        return "Your request method is POST"
    else:
        return '''
        Your request method is GET
        <form action='/methods' method='POST'>
            Press OK!<br>
            <input type='submit' value='OK'/>
        </form>
        '''

# templates, static
@app.route('/user/<name>')
def user(name):
    return render_template("nb_files.html", name=name)

# map multiple urls
@app.route('/logged/')
@app.route('/logged/<name>')
def logged(name=None):
    return render_template("nb_urls.html", logged_name=name)

# passing list
@app.route('/shopping')
def shopping():
    food = ['egg', 'milk', 'cheese', 'bread', 'butter']
    return render_template("nb_list.html", shop=food)

if __name__ == '__main__':
    app.run(debug=True)