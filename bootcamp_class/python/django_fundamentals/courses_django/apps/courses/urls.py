from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^(?P<course_id>\d+)/confirm$', views.confirm, name="confirm"),
    url(r'^(?P<course_id>\d+)/destroy$', views.destroy, name="destroy"),
    # url(r'^(?P<user_id>\d+)/show/$', views.show, name="show"),
    # url(r'^(?P<user_id>\d+)/edit/$', views.edit, name="edit"),
    # url(r'^(?P<user_id>\d+)/update/$', views.show, name="update"),
    # url(r'^(?P<user_id>\d+)/delete/$', views.delete, name="delete"),
    # url(r'^login/$', views.login, name="login"),
    # url(r'^logout/$', views.logout, name="logout"),
]