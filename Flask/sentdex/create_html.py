from content_management import Content
import os

topics_dict = Content()

html_template = '''
{% extends 'header.html' %}

{% block body %}

<body class="body">
    <div class="container" align="left" style="max-width:800px">
        <h2>{{curTitle}}</h2>
        <br>
        <div class="embed-responsive embed-responsive-16by9"></div>

        <p></p>
        <p></p>
        <p></p>
        <p></p>
        
        <kbd data-toggle="collapse" data-target="#consoleinfo" aria-expanded="false" aria-controls="consoleinfo">console</kbd>
        <div class="collapse" id="consoleinfo">
            <div class="well">
                <p>When someone refers to "the console," they are referring to where information from your program is ouput. You will see an example of "output to console" below. If you want this message to go away, just click again on the "console" button that you originally clicked on.</p>
            </div>
        </div>
        <div class="row">
            <div class="col l6">
                <pre  class="prettyprint">
                CODE HERE
                </pre>
            </div>
            <div class="col l6">
                <p>EXPLANATION</p>
            </div>
        </div>
    
        <p>The next tutorial: <a title="{{nextTitle}}" href="{{nextLink}}?completed={{curLink}}"><button class="btn btn-primary">{{nextTitle}}</button></a></p>
    </div>
</body>

{% endblock %}
'''


def convert(arg_str):
    if __name__ == '__main__':
        if __name__ == '__main__':
            return arg_str.\
                replace(' ', '').replace('-', '').\
                replace('(', '').replace(')', '').\
                replace('.', '').replace(',', '').\
                replace('"', '').replace("'", "").\
                replace(':', '').replace('/', '').replace('!', '').replace('?', '').\
                lower()

for subject in topics_dict:
    _subject = 'templates/tutorials/' + convert(subject)
    #print(_subject)

    try:
        os.makedirs(_subject)
        #print('Directory created')
    except:
        pass
        #print('Directory already exists')

    for topic in topics_dict[subject]:
        try:
            filename = convert(topic[0]) + '.html'
            savefile = ''.join([_subject, '/', filename])
            #print(savefile)
            savedata = html_template.replace('%s', subject)
            #print(savedata)
            with open(savefile, 'w') as f:
                f.write(savedata)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    pass