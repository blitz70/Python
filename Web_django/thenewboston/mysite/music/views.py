from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from music.models import Album
from music.forms import UserForm


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


class UserFormView(generic.View):
    form_class = UserForm
    template_name = "music/registration_form.html"

    def get(self, request):  # before submit
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):  # after submit
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect("music:index")
        return redirect(request, self.template_name, {"form": form})
