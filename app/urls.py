from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result/(?P<win>[0-9]+)/$', views.result, name='result'),
]
