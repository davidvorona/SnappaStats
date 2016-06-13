from django.http import HttpResponse
from django.contrib.auth.models import User
import json


def get_user(request, user_id):
    user = User.objects.get(pk=user_id)
    response_payload = {
        'firstname': user.first_name,
        'lastname': user.last_name,
    }
    return HttpResponse(json.dumps(response_payload), content_type='application/json')
