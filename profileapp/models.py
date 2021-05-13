from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/images/%Y/%m/%d/', null=True, blank=True)
    nickname = models.CharField(max_length=20)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nickname
