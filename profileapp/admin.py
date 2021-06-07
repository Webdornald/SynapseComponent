from django.contrib import admin

# Register your models here.
from profileapp.models import Profile, RoleTag

admin.site.register(Profile)
admin.site.register(RoleTag)