from django.conf.urls import url
from . import views

def test(request):
    print "Testing 2"

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^add/(?P<id>\d+)$', views.add),
]