from django.urls import path
import informationapp.views as views

app_name = 'informationapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy')
]