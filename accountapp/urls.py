from django.urls import path

import accountapp.views as views

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),
]