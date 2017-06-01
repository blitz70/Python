from django.views import generic
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
