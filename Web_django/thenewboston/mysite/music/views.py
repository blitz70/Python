from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .models import Album


class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name = "albums"
    model = Album

    '''def get_queryset(self):
        return Album.objects.all()'''


class DetailView(generic.DetailView):
    template_name = "music/detail.html"
    model = Album


class AlbumCreateView(generic.edit.CreateView):
    model = Album
    fields = ["artist", "title", "genre", "logo"]


class AlbumUpdateView(generic.edit.UpdateView):
    model = Album
    fields = ["artist", "title", "genre", "logo"]


class AlbumDeleteView(generic.edit.DeleteView):
    model = Album
    success_url = reverse_lazy("music:index")
