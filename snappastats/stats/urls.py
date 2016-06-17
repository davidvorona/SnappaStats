from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^roster/$', views.roster, name='roster'),
    url(r'^profiles/$', views.profiles, name='profiles'),
    url(r'^input/$', views.data_input, name='data_input'),
]