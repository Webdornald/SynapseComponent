from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project/images/%Y/%m/%d/')
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title