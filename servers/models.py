from django.db import models
from django.contrib.auth.models import User


# from .models import Property

# class Server(models.Model):
#     name        = models.CharField(verbose_name='name', max_length=20, blank=False)
#     is_active   = models.BooleanField(verbose_name= "Active")
#     snooze      = models.DateTimeField(verbose_name='Snooze', auto_now_add=True)
#     ip_address  = models.IPAddressField(verbose_name='IP Address')
#     conx        = models.CharField(verbose_name='Connection String', blank=False, max_length=20)
#     comments    = models.TextField(verbose_name='Comments', max_length=200)
#     is_deleted  = models.BooleanField(verbose_name= "Deleted" )
#     updated_on  = models.DateTimeField(verbose_name='Update On', auto_now=True, auto_now_add=True)
#     updated_by  = models.CharField(verbose_name='Updated By', max_length=20, blank=False)
#     inserted_on = models.DateTimeField(verbose_name='Inserted On', auto_now=False, auto_now_add=True)

#     def __str__(self):
#         return self.name


# class Property(models.Model):
#     code = models.CharField(verbose_name='Code', unique=True,
#                             blank=False, db_index=True, max_length=20)
#     name = models.CharField(verbose_name='Name', max_length=100)
#     is_deleted = models.BooleanField(verbose_name="Deleted")
#     updated_on = models.DateTimeField(verbose_name='Update On', auto_now=True)
#     updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
#     inserted_on = models.DateTimeField(
#         verbose_name='Inserted On', auto_now_add=True)

#     def __str__(self):
#         return self.name


# class Domain(models.Model):
#     name = models.CharField(verbose_name='Name', max_length=20)
#     description = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
