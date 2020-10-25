from django.db import models
# models.py
class User(models.Model,):
    username = models.CharField(max_length=20,blank=True, null=True)
    password = models.CharField(max_length=20,blank=True, null=True)
# Create your models here.
