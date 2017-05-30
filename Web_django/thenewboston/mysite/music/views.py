from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import loader
from .models import Album

# Create your views here.


'''def index(request):
    album_list = Album.objects.all()
    html = "<ul>"
    for album in album_list:
        html += "<li><a href='{url}/'>{title}</a></li>".format(url=str(album.id), title=str(album.title))
    html += "</ul>"
    return HttpResponse(html)'''


'''def index(request):
    album_list = Album.objects.all()
    template = loader.get_template("music/index.html")
    data = {
        "album_list": album_list,
    }
    return HttpResponse(template.render(data, request))'''


def index(request):
    album_list = Album.objects.all()
    return render(request, "music/index.html", {"album_list": album_list})


'''def detail(request, album_id):
    data = {}
    try:
        album = Album.objects.filter(pk=album_id).get()
        data["album"] = album
    except Album.DoesNotExist:
        data["error"] = "Album does not exist!"
    return render(request, "music/detail.html", data)'''


'''def detail(request, album_id):
    data = {}
    try:
        album = Album.objects.filter(pk=album_id).get()
        data["album"] = album
    except Album.DoesNotExist:
        raise Http404("Album does not exist!")
    return render(request, "music/detail.html", data)'''


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, "music/detail.html", {"album": album})


def favorite(request, album_id):
    return None
