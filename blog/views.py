from django.shortcuts import render
from .models import blog
from django.contrib.auth.models import User, auth
# Create your views here.


def index(request):
    blogs = blog.objects.all()
    print(blogs)
    return render(request, 'blog.html', {'blogs': blogs})
