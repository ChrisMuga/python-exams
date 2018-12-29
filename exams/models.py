from django.db import models

# Create your models here.

class User(models.Model):
    first_name      =   models.CharField(max_length=30)
    last_name       =   models.CharField(max_length=30)
    phone_number    =   models.CharField(max_length=15)
    email_address   =   models.CharField(max_length=230)
    password        =   models.CharField(max_length=250)
    