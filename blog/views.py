from django.shortcuts import render
from datetime import date


# Dummy Data
all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Steve",
        "date": date(2024, 12 , 22),
        "title": "Mountain Hiking",
        "excert": "There is nothing like the mountain view when hiking. It's breathtaking.",
        "content": 
            """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Reprehenderit laborum cumque vel sint corporis veniam obcaecati quasi impedit eius alias aspernatur magni nisi iure praesentium, 
            ex perferendis doloremque fugit consectetur.
            """
    },
    {
        "slug": "coding-is-fun",
        "image": "coding.jpg",
        "author": "Steve",
        "date": date(2022, 8 , 12),
        "title": "Coding is fun",
        "excert": "Coding is one of the most fun activites that you can learn things from.",
        "content": 
            """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Reprehenderit laborum cumque vel sint corporis veniam obcaecati quasi impedit eius alias aspernatur magni nisi iure praesentium, 
            ex perferendis doloremque fugit consectetur.
            """
    },
    {
        "slug": "walk-in-the-woods",
        "image": "woods.jpg",
        "author": "Steve",
        "date": date(2023, 9 , 17),
        "title": "A walk in the woods",
        "excert": "A very nice activity that can connect you to nature in one of the most entairtaning ways.",
        "content": 
            """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Reprehenderit laborum cumque vel sint corporis veniam obcaecati quasi impedit eius alias aspernatur magni nisi iure praesentium, 
            ex perferendis doloremque fugit consectetur.
            """
    }
]

def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail-page.html")