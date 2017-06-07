from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # company/stocks
    url(r'^stocks/$', views.StockListView.as_view(), name="stock_list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
