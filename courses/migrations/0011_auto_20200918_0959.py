# Generated by Django 3.1.1 on 2020-09-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]