# Generated by Django 5.0.2 on 2024-02-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_tag_alter_post_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='posts', to='blog.tag'),
        ),
    ]
