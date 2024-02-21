from django.shortcuts import render
from datetime import date
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

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

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail-page.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tag.all()
        context["comments_list"] = self.object.comments_list.all()
        return context

# def posts(request):
#     posts = Post.objects.all()
#     return render(request, "blog/all-posts.html", { "posts": posts })

# def post_detail(request, entered_slug):
#     identified_post = get_object_or_404(Post, slug=entered_slug)
#     return render(request, "blog/post-detail-page.html", {
#         "post": identified_post,
#         "tags": identified_post.tag.all()
#     })