from django.db import models

class admin(models.Model):
    username = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=20) 
    temporary_id = models.CharField(max_length=30) 
    profile_image = models.CharField(max_length=100) 
    role = models.CharField(max_length=200) 

class user(models.Model):
    username = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=20) 
    temporary_id = models.CharField(max_length=30) 
    profile_image = models.CharField(max_length=100) 
    wachlist = models.BooleanField(default=None)
    likeslist = models.BooleanField(default=None)
