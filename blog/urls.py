from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.StartingPageView.as_view() , name="starting_page"),
    path("posts", views.PostsView.as_view(), name="posts"),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name="post_detail"),
    path('read-later', views.ReadLaterView.as_view(), name="read_later"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
