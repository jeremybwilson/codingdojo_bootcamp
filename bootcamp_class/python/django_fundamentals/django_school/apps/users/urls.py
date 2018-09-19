from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.create, name="create"),
    url(r'^new/$', views.new, name="new"),
    # url(r'^show$', views.show, name="show"),  # use this route to show all users?
    url(r'^(?P<user_id>\d+)/show$', views.show, name="show"),
    # url(r'^reset$', views.reset, name="reset"),
]