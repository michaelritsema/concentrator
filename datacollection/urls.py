from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^datacollection$', views.index, name='index'),
    url(r'enqueue$', views.enqueue, name='enqueue'),
    url(r'control/(?P<guid>[^/]+)$', views.dequeue, name='dequeue'),
]