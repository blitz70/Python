from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h2>Hello Django!!</h2>")