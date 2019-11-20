from django.contrib import admin

from .models import Server, Domain, Property

admin.site.register(Server)
admin.site.register(Domain)
admin.site.register(Property)


