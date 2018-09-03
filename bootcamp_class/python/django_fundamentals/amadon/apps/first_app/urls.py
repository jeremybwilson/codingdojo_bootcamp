from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^amadon$', views.index, name="index"),
    url(r'^process$', views.process, name="process"),
    url(r'^amadon/process$', views.process, name="process"),
    url(r'^reset$', views.reset, name="reset"),
    url(r'^amadon/reset$', views.reset, name="reset"),
    url(r'^amadon/checkout$', views.checkout, name="checkout"),
]
