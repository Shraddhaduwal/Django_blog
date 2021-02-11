from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
        # Gets all the posts from the database
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
