from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Server, Domain, Property


class ServerViewAll(ListView):
    template_name = 'server/server.html'
    context_object_name = 'server_list'

    def get_queryset(self):
        return Server.objects.all()


class ServerViewByDomain(ListView):
    template_name = 'server/server.html'
    context_object_name = 'server_list'

    def get_queryset(self):
        self.domain = get_object_or_404(Domain, id=self.kwargs['pk'])
        print(self.domain)
        return Server.objects.filter(domain=self.domain)


class ServerViewByProperty(ListView):
    template_name = 'server/server.html'
    context_object_name = 'server_list'

    def get_queryset(self):
        self.property = get_object_or_404(Property, id=self.kwargs['pk'])
        print(self.property)
        return Server.objects.filter(property=self.property)        


class DomainViewAll(ListView):
    template_name = 'server/domain.html'
    context_object_name = 'domain_list'

    def get_queryset(self):
        return Domain.objects.all()


class PropertyViewAll(ListView):
    template_name = 'server/property.html'
    context_object_name = 'property_list'

    def get_queryset(self):
        return Property.objects.all()
