from django.shortcuts import render
from django.views import generic
from .models import Domain

class DomainView(generic.ListView):
    template_name = 'domain/index.html'
    context_object_name = 'domain_list'

    def get_queryset(self):
        return Domain.objects.all()
