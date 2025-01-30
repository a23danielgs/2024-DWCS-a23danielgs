from django.shortcuts import render
from .models import Post,Tag,Author
from django.shortcuts import render, get_object_or_404
# Create your views here.

def index (request):
    posts = Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html",{"posts":posts})

def detail (request,slug):
    post = get_object_or_404(Post, slug=slug)
    post_tags = post.tag.all()
    return render(request,"blog/detail.html",{"post":post,"tags":post_tags})

def all_posts(request):
    posts = Post.objects.all()
    return render(request,"blog/all_posts.html",{"posts":posts})