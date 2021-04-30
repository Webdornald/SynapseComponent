from django.urls import path
import indexapp.views as views

app_name = 'indexapp'

urlpatterns = [
    path('', views.index, name='index')
]