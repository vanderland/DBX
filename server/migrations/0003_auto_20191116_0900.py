# Generated by Django 2.2.7 on 2019-11-16 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20191115_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]