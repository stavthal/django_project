from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import date
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from blog.forms import CommentForm

# Model
from .models import Post

def get_date(post):
    return post['date']

# Create your views here.
class StartingPageView(View):
    def get(self, request):
        latest_posts = Post.objects.order_by('-date')[:3]
        return render(request, "blog/index.html", {
            "posts": latest_posts
        })
        
class PostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "posts"

class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
          "post": post,
          "post_tags": post.tags.all(),
          "comment_form": CommentForm(),
          "comments": post.comments.all().order_by("-id")
        }
        print(context["comment_form"])
        return render(request, "blog/post-detail-page.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.post = post
          comment.save()

          return HttpResponseRedirect(reverse("post_detail", args=[slug]))

        context = {
          "post": post,
          "post_tags": post.tags.all(),
          "comment_form": comment_form,
          "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail-page.html", context)