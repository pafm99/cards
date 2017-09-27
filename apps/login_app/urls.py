from django.conf.urls import url
from . import views

def test(request):
    print "Testing 2"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    #url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout)
]