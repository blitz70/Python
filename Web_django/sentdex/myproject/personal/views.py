from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'personal/home.html')


def contact(request):
    _contents = {'contents': ["Hi, I'm learning Django with python", "I am @ somewhere"]}
    return render(request, 'personal/basic.html', _contents)
