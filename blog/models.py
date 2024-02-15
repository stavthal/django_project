from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    tag = models.ManyToManyField('Tag', related_name="posts")

    def __str__(self):
        return self.title
    
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    
    def __str__(self):
        return self.caption
    
