from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    code = models.CharField(verbose_name='Code', unique=True,
                            blank=False, db_index=True, max_length=20)
    name = models.CharField(verbose_name='Name', max_length=100)
    is_deleted = models.BooleanField(verbose_name="Deleted")
    updated_on = models.DateTimeField(verbose_name='Update On', auto_now=True)
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    inserted_on = models.DateTimeField(
        verbose_name='Inserted On', auto_now_add=True)

    def __str__(self):
        return self.name