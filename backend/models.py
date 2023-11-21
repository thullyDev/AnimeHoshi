# from django.contrib.auth.models import User
from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=80, unique=True)
    email = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=20) 
    temporary_id = models.CharField(max_length=30, unique=True) 
    profile_image = models.CharField(max_length=100) 
    role = models.CharField(max_length=200) 
    deleted = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, unique=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, unique=True)

    class Meta:
        # ordering = ("+username",)
        app_label = 'backend'

    def _str_(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=80, unique=True)
    email = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=20) 
    temporary_id = models.CharField(max_length=30, unique=True) 
    profile_image = models.CharField(max_length=100, null=True, blank=True) 
    wachlist = models.BooleanField(null=True, blank=True)
    likeslist = models.BooleanField(null=True, blank=True)
    deleted = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False,unique=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, unique=True)

    class Meta:
        # ordering = ("+username",)
        app_label = 'backend'

    def _str_(self):
        return self.name
