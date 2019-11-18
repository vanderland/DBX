from django.urls import path

from . import views

# app_name = 'domain'
urlpatterns = [
    path('', views.DomainView.as_view(), name='domain'),
  ]
