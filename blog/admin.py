from django.contrib import admin

from .models import Post

# Register your models here.

# add me a filter for the PostAdmin
class PostAdmin(admin.ModelAdmin):
    # add me a filter for the PostAdmin
    list_display = ("title", "slug", "date")
    # add me more sections for the PostAdmin
    list_filter = ("date",)
    # add me a search bar for the PostAdmin
    search_fields = ("title", "content")
    # add me prefilled fields for the Post
    prepopulated_fields = {"slug": ("title",)}
    
    
admin.site.register(Post, PostAdmin)