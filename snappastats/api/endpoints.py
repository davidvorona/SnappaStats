from django.http import HttpResponse
from django.contrib.auth.models import User
from stats.models import Profile
import json

import random


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
            'id': profile.pk,
            'hometown': profile.hometown,
            'description': profile.description,
        } for profile in profiles
    ]
    return HttpResponse(json.dumps(response_payload), content_type='application/json')


def get_profile(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)

    rp = random.randint(10, 40)
    rn = random.randint(10, 40)
    rm = 100 - rp - rn

    response_payload = {
        'firstname': profile.firstname,
        'lastname': profile.lastname,
        'id': profile.pk,
        'hometown': profile.hometown,
        'description': profile.description,
        'games': profile.players.count(),
        'points': sum([player.points for player in profile.players.all()]),
        'sinks': sum([player.sinks for player in profile.players.all()]),
        'throwing': random.randint(10, 90),  # TODO make real
        'catching': random.randint(10, 90),  # TODO make real
        'breakdown': {
            'points': rp,
            'normal': rn,
            'misses': rm,
        },
    }
    return HttpResponse(json.dumps(response_payload), content_type='application/json')


def get_names_dict(request):
    profiles = Profile.objects.all()
    response_payload = {}
    for profile in profiles:
        response_payload[profile.firstname.lower()] = profile.pk
        response_payload[profile.lastname.lower()] = profile.pk
        response_payload['{} {}'.format(profile.firstname, profile.lastname).lower()] = profile.pk
    return HttpResponse(json.dumps(response_payload), content_type='application/json')

