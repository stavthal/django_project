from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(default=None, null=True, blank=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tag = models.ManyToManyField('Tag', related_name="posts")
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    last_updated = models.DateTimeField(auto_now=True)

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
    
