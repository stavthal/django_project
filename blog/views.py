from django.shortcuts import render
from datetime import date
from django.shortcuts import render, get_object_or_404


# Model
from .models import Post

def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    # sorted_posts = sorted(all_posts, key=get_date)
    posts = Post.objects.all()
    latest_posts = Post.objects.order_by('-date')[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    posts = Post.objects.all()
    return render(request, "blog/all-posts.html", { "posts": posts })

def post_detail(request, entered_slug):
    identified_post = get_object_or_404(Post, slug=entered_slug)
    return render(request, "blog/post-detail-page.html", {
        "post": identified_post,
        "tags": identified_post.tag.all()
    })