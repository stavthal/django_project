from . import views
from django.urls import path

urlpatterns = [
    path('', views.starting_page , name="starting_page"),
    path("posts", views.posts, name="posts"),
    path('post/<slug:slug>/', views.post_detail, name="post_detail"),
]
