from django.db import models

# Create your models here.

class Item(models.Model):
    sname = models.CharField(max_length=100, null=True)
    fname = models.CharField(max_length=100, null=True)
    mname = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    birthday = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)