from django.contrib.auth.models import User
from django.db import models

from profileapp.models import Profile


class Project(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)
    index = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project/images/%Y/%m/%d/')
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    participants = models.ManyToManyField(Profile, blank=True, related_name='participants')

    def __str__(self):
        return self.title