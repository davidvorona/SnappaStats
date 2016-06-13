from django.conf.urls import url, include

from . import endpoints

v1_patterns = [
    url(r'^get/user/(?P<user_id>[0-9]+)/', endpoints.get_user),
]

urlpatterns = [
    url(r'^v1/', include(v1_patterns)),
]
