from django.contrib import admin

from .models import Server, Domain, Property, Application, LoginProfile

admin.site.register(Domain)
admin.site.register(Property)
admin.site.register(Application)
admin.site.register(LoginProfile)
admin.site.register(Server)
