# Generated by Django 4.2 on 2024-05-03 12:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_remove_post_created_at_remove_post_updated_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='link',
            new_name='url',
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]