from django.urls import path

from .views import ServerViewAll, ServerViewByDomain, ServerViewByProperty, ServerViewByApplication, DomainViewAll, PropertyViewAll, ApplicationViewAll, ServerDetail


urlpatterns = [
    path('', ServerViewAll.as_view(), name='server_all'),
    # path('', test, name='server_all'),
    path('domain/', DomainViewAll.as_view(), name='domain_all'),
    path('property/', PropertyViewAll.as_view(), name='property_all'),
    path('application/', ApplicationViewAll.as_view(), name='application_all'),

    path('domain/<int:pk>', ServerViewByDomain.as_view(), name='server_by_domain'),
    path('property/<int:pk>', ServerViewByProperty.as_view(), name='server_by_property'),
    path('application/<int:pk>', ServerViewByApplication.as_view(), name='server_by_application'),

    # path('<int:pk>', ServerDetailView.as_view(), name='server_detail'),
    path('<int:server_id>', ServerDetail, name='server_detail'),
    path('<int:server_id>/<group>/<int:group_id>', ServerDetail, name='server_detail'),

]
