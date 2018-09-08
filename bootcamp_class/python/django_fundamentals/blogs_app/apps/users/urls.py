from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users', views.index),                               # we added this line
    url(r'^users/register$', views.register),                   # we added this line
    url(r'^users/login$', views.login),
    url(r'^users/new$', views.new),                      # we added this line
    # url(r'^blogs/(?P<number>\d+)$', views.show),                # we added this line
    # url(r'^blogs/(?P<number>\d+)/edit$', views.edit),           # we added this line
    # url(r'^blogs/(?P<number>\d+)/delete$', views.destroy),       # we added this line
]