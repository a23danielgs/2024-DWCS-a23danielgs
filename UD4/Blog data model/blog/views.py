from django.shortcuts import render
from .models import Post,Tag,Author
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class Index (ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"

    def get_queryset (self):
        return Post.objects.all().order_by("-date")[:3]

class PostsList (ListView):
    template_name = "blog/all_posts.html"
    model = Post
    context_object_name = "posts"

    def get_queryset (self):
        return Post.objects.all().order_by("-date")

class Detail (View):
    # template_name = "blog/detail.html"
    # model = Post

    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/detail.html",context)

    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("blog:detail",args=[slug]))
        
        context = {
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/detail.html",context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["tags"] = self.object.tag.all()
    #     context["comment_form"] = CommentForm()
    #     return context

class ReadLater (View):
    def get (self,request):
        posts = request.session.get("read_later_posts")
        context = {}

        if posts is None or len(posts)==0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            read_later_posts = Post.objects.filter(id__in=posts)
            context["posts"] = read_later_posts
            context["has_posts"] = True

        return HttpResponseRedirect("/read-later")

    def post(self,request):
        post_id = int(request.POST["post_id"])
        post_slug = request.POST["post_slug"]
        read_later_posts = request.session.get("read_later_posts",[])

        if post_id not in read_later_posts:
            read_later_posts.append(post_id)
            request.session['read_later_posts'] = read_later_posts

        return HttpResponseRedirect(reverse('blog:detail', args=[post_slug]))

