# Generated by Django 3.2 on 2021-05-04 17:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectapp', '0002_project_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]