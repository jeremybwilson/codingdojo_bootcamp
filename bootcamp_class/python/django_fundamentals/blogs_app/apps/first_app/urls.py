from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs_app$', views.index),                               # we added this line
    url(r'^blogs_app/new$', views.new),                             # we added this line
    url(r'^blogs_app/create$', views.create),                       # we added this line
    url(r'^blogs_app/(?P<number>\d+)$', views.show),                # we added this line
    url(r'^blogs_app/(?P<number>\d+)/edit$', views.edit),           # we added this line
    url(r'^blogs_app/(?P<number>\d+)/delete$', views.destroy),       # we added this line
]