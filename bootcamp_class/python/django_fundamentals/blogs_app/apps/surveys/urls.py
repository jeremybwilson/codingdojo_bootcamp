from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys', views.index),                               # we added this line
    url(r'^surveys/new$', views.new),                             # we added this line
    # url(r'^surveys/(?P<number>\d+)$', views.show),                # we added this line
    # url(r'^surveys/(?P<number>\d+)/edit$', views.edit),           # we added this line
    # url(r'^surveys/(?P<number>\d+)/delete$', views.destroy),       # we added this line
]