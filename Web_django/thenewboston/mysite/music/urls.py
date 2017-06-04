from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^album/add/$', views.AlbumCreateView.as_view(), name="add_album"),
    url(r'^album/(?P<pk>\d+)/$', views.AlbumUpdateView.as_view(), name="update_album"),
    url(r'^album/(?P<pk>\d+)/delete/$', views.AlbumDeleteView.as_view(), name="delete_album"),
    # url(r'^$', views.index, name="index"),  # /
    # url(r'^(?P<pk>[0-9]+)/$', views.detail, name="detail"),  # /<pk>/
    # url(r'^(?P<pk>[0-9]+)/favorite/$', views.favorite, name="favorite"),  # /<pk>/favorite
    # url(r'^album/add/$', views.add_album, name="add_album"),
]
