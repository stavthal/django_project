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
    def is_stored(self, request, post_id):
        stored_posts = request.session.get("stored_posts") # Get the stored posts from the session
        if stored_posts is not None: # If there are no stored posts
          is_saved_for_later = post_id in stored_posts # Check if the post is stored for later
        else: # If there are stored posts
          is_saved_for_later = False # Set is_saved_for_later to False
          
        return is_saved_for_later
      
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
 
        context = {
          "post": post,
          "post_tags": post.tags.all(),
          "comment_form": CommentForm(),
          "comments": post.comments.all().order_by("-id"),
          "saved_for_later": self.is_stored(request, post.id)
        }
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
          "comments": post.comments.all().order_by("-id"),
          "is_saved_for_later": self.is_stored(request, post.id)
        }
        return render(request, "blog/post-detail-page.html", context)
      
class ReadLaterView(View):
  def get(self,request):
    stored_posts = request.session.get("stored_posts") # Get the stored posts from the session
    
    context = {} # Create a context dictionary
    
    if stored_posts is None or len(stored_posts) == 0: # If there are no stored posts
      context["posts"] = [] # If there are no stored posts, set the posts to an empty list
      context["has_posts"] = False # Set has_posts to False
    else:
      posts = Post.objects.filter(id__in=stored_posts) # Get all the posts that have their id in the list of stored posts
      context["posts"] = posts
      context["has_posts"] = True
    
    return render(request, "blog/stored-posts.html", context) # Render the stored-posts.html template with the context dictionary
    
  
  def post(self,request):
    stored_posts = request.session.get("stored_posts") # Get the stored posts from the session
    
    if stored_posts is None: # If there are no stored posts
      stored_posts = [] # Set the stored posts to an empty list
      
    post_id = request.POST["post_id"] # Get the id of the post that the user wants to store
    
    if post_id in stored_posts: # If the post is already stored
      stored_posts.remove(post_id)
    else: # If the post is not stored
      stored_posts.append(post_id) # Add the new post to the list of stored posts
    
    request.session["stored_posts"] = stored_posts # Set the stored posts to the list of stored posts in the session
      
    return HttpResponseRedirect("/") # Redirect the user to the homepage