from django.shortcuts import render


def testpage(request):
    return render(request, 'stats/testpage.html')


def home(request):
    return render(request, 'stats/home.html')


def roster(request):
    return render(request, 'stats/roster.html')


def profiles(request):
    return render(request, 'stats/profiles.html')
