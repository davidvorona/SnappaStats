from django.conf.urls import url, include

from . import endpoints

v1_patterns = [
    url(r'^get/user/(?P<user_id>[0-9]+)/', endpoints.get_user),
    url(r'^get/profiles/$', endpoints.get_profiles),
]

urlpatterns = [
    url(r'^v1/', include(v1_patterns)),
]
