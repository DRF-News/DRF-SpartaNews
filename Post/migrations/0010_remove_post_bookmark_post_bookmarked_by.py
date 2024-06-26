# Generated by Django 4.2 on 2024-05-07 08:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Post', '0009_remove_post_username_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='bookmark',
        ),
        migrations.AddField(
            model_name='post',
            name='bookmarked_by',
            field=models.ManyToManyField(blank=True, related_name='bookmarked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
