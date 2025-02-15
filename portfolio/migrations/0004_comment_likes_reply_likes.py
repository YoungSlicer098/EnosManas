# Generated by Django 5.0.4 on 2024-04-09 10:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_urlpost_webpage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='comments_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reply',
            name='likes',
            field=models.ManyToManyField(related_name='reply_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
