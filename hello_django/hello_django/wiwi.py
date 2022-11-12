from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    a = 7 + 9
    return render(request, 'about.html', {'kredit': a})


def home(request):
    return HttpResponse('This is my Home')

