from django.http import HttpResponse
from django.contrib.auth.models import User
from stats.models import Profile
from stats.processing import digest, generate_game
from django.views.decorators.csrf import csrf_exempt
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
    points_normalized = round(profile.digested_stats.points * 100 / profile.digested_stats.shots)
    misses_normalized = round(profile.digested_stats.misses * 100 / profile.digested_stats.shots)
    normal_normalized = 100 - points_normalized - misses_normalized
    response_payload = {
        'firstname': profile.firstname,
        'lastname': profile.lastname,
        'id': profile.pk,
        'hometown': profile.hometown,
        'description': profile.description,
        'games': profile.digested_stats.games,
        'points': profile.digested_stats.points,
        'sinks': profile.digested_stats.sinks,
        'throwing': profile.digested_stats.throwing_score,
        'catching': profile.digested_stats.catching_score,
        'breakdown': {
            'points': points_normalized,
            'normal': normal_normalized,
            'misses': misses_normalized,
        },
    }
    return HttpResponse(json.dumps(response_payload), content_type='application/json')


def get_names_dict(request):
    fullnames_only = request.GET.get('fullnames_only', False)
    profiles = Profile.objects.all()
    response_payload = {}
    for profile in profiles:
        if not fullnames_only:
            response_payload[profile.firstname.lower()] = profile.pk
            response_payload[profile.lastname.lower()] = profile.pk
        response_payload['{} {}'.format(profile.firstname, profile.lastname).lower()] = profile.pk
    return HttpResponse(json.dumps(response_payload), content_type='application/json')


def digest_profile(request, profile_id):
    digest(profile_id)
    return HttpResponse(200)


@csrf_exempt
def add_game(request):
    if request.method != 'POST':
        return HttpResponse('POST request required.', status=403)
    profile_ids = generate_game(json.loads(request.body.decode('utf-8'))['data'])
    for id in profile_ids:
        digest(id)
    return HttpResponse(200)

