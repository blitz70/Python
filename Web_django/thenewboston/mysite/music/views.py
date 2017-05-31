from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Album, Song

# Create your views here.


def index(request):
    album_list = Album.objects.all()
    return render(request, "music/index.html", {"album_list": album_list})


def detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "music/detail.html", {"album": album})


def favorite(request, pk):
    album = get_object_or_404(Album, pk=pk)
    try:
        song = album.song_set.get(pk=request.POST["song"])
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except Song.DoesNotExist:
        error_message = "Something went wrong"
        return render(request, "music/detail.html", {"album": album, "error_message": error_message})
    return render(request, "music/detail.html", {"album": album})

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
    return HttpResponse(template.render({"album_list": album_list}, request))'''


'''def detail(request, pk):
    data = {}
    try:
        album = Album.objects.filter(pk=pk).get()
        data["album"] = album
    except Album.DoesNotExist:
        data["error"] = "Album does not exist!"
    return render(request, "music/detail.html", data)'''


'''def detail(request, pk):
    try:
        album = Album.objects.filter(pk=pk).get()
        return render(request, "music/detail.html", {"album": album})
    except Album.DoesNotExist:
        raise Http404("Album does not exist!")'''

