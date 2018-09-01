from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^surveys$', views.index, name="index"),
    url(r'^surveys/results$', views.results, name="results")
]
