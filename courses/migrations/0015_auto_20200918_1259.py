# Generated by Django 3.1.1 on 2020-09-18 12:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0014_auto_20200918_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='review_dislikes',
            field=models.ManyToManyField(blank=True, related_name='review_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviews',
            name='review_likes',
            field=models.ManyToManyField(blank=True, related_name='review_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='course_rating',
            field=models.IntegerField(default=0),
        ),
    ]