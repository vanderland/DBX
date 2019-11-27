from django.urls import path

from .views import ServerViewAll, ServerViewByDomain, ServerViewByProperty, DomainViewAll, PropertyViewAll, ServerDetail


urlpatterns = [
    path('', ServerViewAll.as_view(), name='server_all'),
    # path('', test, name='server_all'),
    path('domain/', DomainViewAll.as_view(), name='domain_all'),
    path('property/', PropertyViewAll.as_view(), name='property_all'),

    path('domain/<int:pk>', ServerViewByDomain.as_view(), name='server_by_domain'),
    path('property/<int:pk>', ServerViewByProperty.as_view(),
         name='server_by_property'),

    # path('<int:pk>', ServerDetailView.as_view(), name='server_detail'),
    path('<int:pk>', ServerDetail, name='server_detail'),

]
