from django.urls import path

from contactapp import views

app_name = 'contactapp'

urlpatterns = [
    path('', views.index, name='index')
]