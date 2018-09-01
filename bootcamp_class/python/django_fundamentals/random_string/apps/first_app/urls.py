from django.conf.urls import url
from . import views      

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^random_word$', views.index, name="index"),
    url(r'^random_word/attempt$', views.attempt, name="attempt"),
    url(r'^random_word/reset$', views.reset, name="reset")
]