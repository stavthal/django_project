# Generated by Django 5.0.2 on 2024-02-26 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_comment_author_remove_comment_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]
