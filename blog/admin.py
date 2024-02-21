from django.contrib import admin

from .models import Post, Author, Tag, Comment

# Register your models here.

# add me a filter for the PostAdmin
class PostAdmin(admin.ModelAdmin):
    # add me a filter for the PostAdmin
    readonly_fields = ("date", "last_updated")
    list_display = ("title", "slug", "date")
    # add me more sections for the PostAdmin
    list_filter = ("date",)
    # add me a search bar for the PostAdmin
    search_fields = ("title", "content")
    # add me prefilled fields for the Post
    prepopulated_fields = {"slug": ("title",)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    list_filter = ("last_name",)
    search_fields = ("first_name", "last_name")
    
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Comment)