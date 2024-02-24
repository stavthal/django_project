from django import forms

from blog.models import Post


class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['post', '']
        labels = {
            "content": "Comment Title",
            "author": "Your name",
        }