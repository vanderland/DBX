from django.urls import path

from .views import ServerViewAll, ServerViewByDomain, ServerViewByProperty, DomainViewAll, PropertyViewAll

# app_name = 'property'
urlpatterns = [
    path('', ServerViewAll.as_view(), name='server_all'),
    path('domain/', DomainViewAll.as_view(), name='domain_all'),
    path('property/', PropertyViewAll.as_view(), name='property_all'),

    path('domain/<int:pk>', ServerViewByDomain.as_view(), name='server_by_domain'),
    path('property/<int:pk>', ServerViewByProperty.as_view(), name='server_by_property'),

  ]
