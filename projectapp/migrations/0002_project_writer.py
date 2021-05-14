# Generated by Django 3.2 on 2021-05-03 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project', to=settings.AUTH_USER_MODEL),
        ),
    ]
