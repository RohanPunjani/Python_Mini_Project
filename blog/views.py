from django.shortcuts import render
from .models import blog
from django.contrib.auth.models import User, auth
# Create your views here.


def index(request):
    if(request.user.is_authenticated):
        user = request.user
        blogs = user.blog_set.all()
        return render(request, 'blog.html', {'blogs': blogs})
    else:
        return render(request, 'blog.html', {'blogs': None})


def blog_view(request, id):
    if(request.user.is_authenticated):
        user = request.user
        blog = user.blog_set.get(id=id)
        return render(request, 'content.html', {'blog': blog})
    else:
        return render(request, 'content.html', {'blog': None})
