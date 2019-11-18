from django.db import models

class Domain(models.Model):
    name = models.CharField(verbose_name='Name', max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

