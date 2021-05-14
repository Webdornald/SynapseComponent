from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['index', 'title', 'image', 'content', 'participants']
        widgets = {
            'content': SummernoteWidget(),
        }