from django.conf.urls import url
from . import views

app_name = "ns_music"

urlpatterns = [
    url(r'^$', views.index, name="index"),  # /
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name="detail"),  # /<pk>/
    url(r'^(?P<pk>[0-9]+)/favorite/$', views.favorite, name="favorite"),  # /<pk>/favorite
]
