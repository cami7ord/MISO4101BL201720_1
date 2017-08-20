from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):

   user = models.OneToOneField(User)
   country = models.CharField(max_length=256, blank=False, null=False)
   city = models.CharField(max_length=256, blank=False, null=False)
   interests = models.CharField(max_length=256, blank=False, null=False)

class Category(models.Model):
   name = models.CharField(max_length=256, blank=False, null=False)


