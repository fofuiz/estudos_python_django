from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone


def index(request):
    return HttpResponse("A senha é Hiramuki!")

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

