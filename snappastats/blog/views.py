from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogEntry


def testpage(request):
    entries = BlogEntry.objects.all()
    multiple_entries = len(entries) > 1
    return render(request, 'blog/testpage.html', {
        'entries': entries,
        'multiple_entries': multiple_entries
    })
