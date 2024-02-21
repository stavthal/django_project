from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.starting_page , name="starting_page"),
    path("posts", views.posts, name="posts"),
    path('post/<slug:entered_slug>/', views.post_detail, name="post_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
