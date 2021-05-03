from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from projectapp.models import Project


class ProjectModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Project, ProjectModelAdmin)
