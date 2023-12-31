# Generated by Django 4.2.3 on 2023-07-11 11:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_post_category_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='followedID',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='followerID',
        ),
        migrations.AddField(
            model_name='follow',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='follows', to=settings.AUTH_USER_MODEL),
        ),
    ]
