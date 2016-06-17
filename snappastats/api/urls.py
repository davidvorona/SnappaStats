from django.conf.urls import url, include

from . import endpoints

v1_patterns = [
    url(r'^get/user/(?P<user_id>[0-9]+)/', endpoints.get_user),
    url(r'^get/profiles/$', endpoints.get_profiles),
    url(r'^get/profile/(?P<profile_id>[0-9]+)/$', endpoints.get_profile),
    url(r'^get/names_dict/$', endpoints.get_names_dict),
    url(r'^digest/profile/(?P<profile_id>[0-9]+)/', endpoints.digest_profile),
    url(r'^digest/all/$', endpoints.digest_all),
    url(r'^add/game/', endpoints.add_game),
]

urlpatterns = [
    url(r'^v1/', include(v1_patterns)),
]
