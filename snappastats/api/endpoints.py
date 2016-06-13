from django.shortcuts import render
from django.http import HttpResponse


def get_user(request, user_id):
    return HttpResponse(200)
