# Generated by Django 3.2 on 2021-06-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0003_profile_participation'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='role_tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='roletag', to='profileapp.RoleTag'),
        ),
    ]
