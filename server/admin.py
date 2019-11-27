from django.contrib import admin

from .models import Server, Domain, Property, Application

admin.site.register(Domain)
admin.site.register(Property)
admin.site.register(Application)
admin.site.register(Server)
