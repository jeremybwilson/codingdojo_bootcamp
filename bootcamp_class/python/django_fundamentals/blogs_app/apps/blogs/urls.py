from django.conf.urls import url
# from . import views
from views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="index"),
    url(r'^blogs', HomeView.as_view(), name="blogs"),                   # we added this line
    # url(r'^blogs/new$', HomeView.as_view()),                          # we added this line
    url(r'^blogs/process$', HomeView.as_view()),                       # we added this line
    # url(r'^blogs/(?P<number>\d+)$', views.HomeView.as_view()),              # we added this line
    # url(r'^blogs/(?P<number>\d+)/edit$', views.HomeView.as_view()),         # we added this line
    # url(r'^blogs/(?P<number>\d+)/delete$', views.HomeView.as_view()),       # we added this line
]