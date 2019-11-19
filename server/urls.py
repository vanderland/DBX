from django.urls import path

from . import views

# app_name = 'property'
urlpatterns = [
    path('', views.ServerView.as_view(), name='server'),
  ]
