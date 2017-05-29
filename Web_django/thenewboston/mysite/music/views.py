from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Album

# Create your views here.


'''def index(request):
    album_list = Album.objects.all()
    html = "<ul>"
    for album in album_list:
        html += "<li><a href='{url}/'>{title}</a></li>".format(url=str(album.id), title=str(album.title))
    html += "</ul>"
    return HttpResponse(html)'''


def index(request):
    album_list = Album.objects.all()
    template = loader.get_template("music/index.html")
    data = {
        "album_list": album_list,
    }
    return HttpResponse(template.render(data, request))


def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id:" + str(album_id) + "</h2>")
