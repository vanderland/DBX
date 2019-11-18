from django.shortcuts import render
from django.views import generic
from .models import Property


class PropertyView(generic.ListView):
    template_name = 'property/index.html'
    context_object_name = 'property_list'

    def get_queryset(self):
        return Property.objects.all()

class PropertyDetailView(generic.DetailView):
    model = Property
    template_name = 'property/property.html'
