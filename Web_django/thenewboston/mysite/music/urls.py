from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),  # /
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),  # /<pk>/
    url(r'^album/add/$', views.add_album, name="add_album")
]

'''urlpatterns = [
    url(r'^$', views.index, name="index"),  # /
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name="detail"),  # /<pk>/
    url(r'^(?P<pk>[0-9]+)/favorite/$', views.favorite, name="favorite"),  # /<pk>/favorite
]'''
