from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    name = models.CharField(verbose_name='Name', max_length=20)
    description = models.CharField(verbose_name='Description', max_length=100)
    updated_on = models.DateTimeField(verbose_name='Update On', auto_now=True)
    updated_by = models.ForeignKey(User, verbose_name='Update By', null=True, on_delete=models.CASCADE)
    inserted_on = models.DateTimeField(verbose_name='Inserted On', auto_now_add=True)
    manager = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'


class Domain(models.Model):
    name = models.CharField(verbose_name='Name', max_length=20)
    description = models.CharField(verbose_name='Description', max_length=100)
    updated_on = models.DateTimeField(verbose_name='Update On', auto_now=True)
    updated_by = models.ForeignKey(User, verbose_name='Update By', null=True, on_delete=models.CASCADE)
    inserted_on = models.DateTimeField(verbose_name='Inserted On', auto_now_add=True)
    manager = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Domain'
        verbose_name_plural = 'Domains'


class Property(models.Model):
    code = models.CharField(verbose_name='Code', unique=True, blank=False, db_index=True, max_length=20)
    name = models.CharField(verbose_name='Name', max_length=100)
    updated_on = models.DateTimeField(verbose_name='Update On', auto_now=True)
    updated_on = models.DateTimeField(verbose_name='Update On', auto_now=True)
    updated_by = models.ForeignKey(User, verbose_name='Update By', null=True, on_delete=models.CASCADE)
    inserted_on = models.DateTimeField(verbose_name='Inserted On', auto_now_add=True)
    manager = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        # indexes = [models.Index(fields=['full_name'])]
        ordering = ['name']
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class LoginProfile(models.Model):
    name = models.CharField(verbose_name='name', max_length=20, blank=False)
    login = models.CharField(verbose_name='Login', blank=False, max_length=20)
    passwd = models.CharField(verbose_name='Password', blank=False, max_length=50)
    comments = models.TextField(verbose_name='Comments', max_length=200)
    updated_on = models.DateTimeField(verbose_name='Update On', auto_now=True)
    updated_by = models.ForeignKey(User, verbose_name='Update By', null=True, on_delete=models.CASCADE)
    inserted_on = models.DateTimeField(verbose_name='Inserted On', auto_now_add=True)
    manager = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Login Profile'
        verbose_name_plural = 'Login Profiles'


class Server(models.Model):
    name = models.CharField(verbose_name='name', max_length=20, blank=False)
    ip_address = models.GenericIPAddressField(verbose_name='IP Address')
    login_profile = models.ForeignKey(LoginProfile, verbose_name='Login Profile', null=True, on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain, verbose_name='Domain', null=True, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, verbose_name='Property', null=True, on_delete=models.CASCADE)
    application = models.ManyToManyField(Application, verbose_name='Applications', null=True)
    comments = models.TextField(verbose_name='Comments', max_length=200)
    is_active = models.BooleanField(verbose_name="Active", default=1)
    updated_on = models.DateTimeField(verbose_name='Update On', auto_now=True)
    updated_by = models.ForeignKey(User, verbose_name='Update By', null=True, on_delete=models.CASCADE)
    inserted_on = models.DateTimeField(verbose_name='Inserted On', auto_now_add=True)
    manager = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Server'
        verbose_name_plural = 'Servers'
