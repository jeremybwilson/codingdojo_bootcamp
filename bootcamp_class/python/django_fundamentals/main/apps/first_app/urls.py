from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),  # we added this line
    url(r'^test$', views.test),  # we added this line
    url(r'^2003/$', views.special_case_2003),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<word>\w+)$', views.show_word),
    url(r'^(?P<year>[0-9]{4})/$', views.year_archive),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
]