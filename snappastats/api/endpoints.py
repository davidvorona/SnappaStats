from django.http import HttpResponse
from django.contrib.auth.models import User
from stats.models import Profile
import json


def get_user(request, user_id):
    user = User.objects.get(pk=user_id)
    response_payload = {
        'firstname': user.first_name,
        'lastname': user.last_name,
    }
    return HttpResponse(json.dumps(response_payload), content_type='application/json')


def get_profiles(request):
    profiles = Profile.objects.all()
    response_payload = [
        {
            'firstname': profile.firstname,
            'lastname': profile.lastname,
        } for profile in profiles
    ]
    return HttpResponse(json.dumps(response_payload), content_type='application/json')

