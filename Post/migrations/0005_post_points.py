# Generated by Django 4.2 on 2024-05-07 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_remove_post_points_remove_post_bookmark_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='points',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
