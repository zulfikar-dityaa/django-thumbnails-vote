from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_thumbnails, name='add'),
    path('register/', views.register, name='register'),
    path('login_status/', views.login_status, name='login_status'),
    path('detail/<int:id_pool>/', views.detail, name='detail'),
]