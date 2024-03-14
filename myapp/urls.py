from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('users/<name>/<int:id>', views.users, name='users'),
    path('users/', views.getuser, name='getuser'),
]