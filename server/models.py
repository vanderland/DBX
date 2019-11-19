from django.db import models
from django.contrib.auth.models import User
from property.models import Property
from domain.models import Domain


class Server(models.Model):
    name        = models.CharField(verbose_name='name', max_length=20, blank=False)
    is_active   = models.BooleanField(verbose_name= "Active")
    snooze      = models.DateTimeField(verbose_name='Snooze', auto_now_add=True)
    ip_address  = models.GenericIPAddressField(verbose_name='IP Address')
    conn_str    = models.CharField(verbose_name='Connection String', blank=False, max_length=20)
    comments    = models.TextField(verbose_name='Comments', max_length=200)
    domain      = models.ForeignKey(Domain, null=True, on_delete=models.CASCADE)
    property    = models.ForeignKey(Property, null=True, on_delete=models.CASCADE)
    updated_on  = models.DateTimeField(verbose_name='Update On', auto_now=True)
    updated_by  = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    inserted_on = models.DateTimeField(
        verbose_name='Inserted On', auto_now_add=True)

    def __str__(self):
        return self.name