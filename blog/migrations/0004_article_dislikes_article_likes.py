# Generated by Django 4.1.5 on 2023-02-04 12:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='dislikes',
            field=models.ManyToManyField(related_name='article_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(related_name='article_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]