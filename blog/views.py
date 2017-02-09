from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("A senha é Hiramuki!")

def hira(request):
    return render(request, 'blog/hira.html', {})

def josefina(request):
    return render(request, 'blog/josefina.html', {})