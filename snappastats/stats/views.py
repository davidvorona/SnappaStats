from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def testpage(request):
    return render(request, 'stats/testpage.html')


def home(request):
    return render(request, 'stats/home.html')


def roster(request):
    return render(request, 'stats/roster.html')


def profiles(request):
    return render(request, 'stats/profiles.html')


@login_required
def data_input(request):
    return render(request, 'stats/data_input.html')

