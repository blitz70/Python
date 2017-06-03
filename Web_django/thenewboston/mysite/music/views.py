from django.views import generic
from .models import Album
from django.shortcuts import render
from datetime import date as d


class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name = "albums"
    model = Album

    '''def get_queryset(self):
        return Album.objects.all()'''


class DetailView(generic.DetailView):
    template_name = "music/detail.html"
    model = Album


def add_album(request):
    if request.method == "POST":
        artist = request.POST["artist"]
        title = request.POST["title"]
        genre = request.POST["genre"]
        logo = request.POST["logo"]
        album = Album(artist=artist, title=title, genre=genre, logo=logo, date=d.today())
        album.save()
        return render(request, "music/detail.html", {"album": album})
    return render(request, "music/add_album.html")
