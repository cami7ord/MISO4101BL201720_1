from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

CLASIFICATION_CHOICES = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
)

class UserProfile(models.Model):

   user = models.OneToOneField(User)
   country = models.CharField(max_length=256, blank=False, null=False)
   city = models.CharField(max_length=256, blank=False, null=False)
   interests = models.CharField(max_length=256, blank=False, null=False)

class Category(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.name

class Species(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    clasification = CLASIFICATION_CHOICES
    scientific_name = models.CharField(max_length=256, blank=False, null=False)
    category = models.ForeignKey(Category)
    picture = models.ImageField(upload_to='images', null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.scientific_name

class Comment(models.Model):
    species = models.ForeignKey(Species)
    email = models.CharField(max_length=256, blank=False, null=False)
    text = models.TextField(blank=True, null=True)
