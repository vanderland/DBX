# from django.shortcuts import render
# # from django.urls import reverse
# from django.views import generic
# from .models import Property, Domain


# class PropertyView(generic.ListView):
#     template_name = 'servers/property.html'
#     context_object_name = 'property_list'

#     def get_queryset(self):
#         return Property.objects.all()


# class DomainView(generic.ListView):
#     template_name = 'servers/domain.html'
#     context_object_name = 'domain_list'

#     def get_queryset(self):
#         return Domain.objects.all()

# class PropertyDetailView(generic.DetailView):
#     model = Property
#     template_name = 'servers/property.html'





# # def property_view(request):
# #     return render(request, "servers/property.html")

