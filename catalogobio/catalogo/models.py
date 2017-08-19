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

class Categoria(models.Model):
   nombre = models.CharField(max_length=256, blank=False, null=False)

class Especie(models.Model):
    nombre = models.CharField(max_length=256, blank=False, null=False)
    clasificacion = CLASIFICATION_CHOICES
    nombre_cientifico = models.CharField(max_length=256, blank=False, null=False)
    categoria = models.ForeignKey(Categoria)
    foto = models.CharField(max_length=256, blank=False, null=False)
    descripcion = models.CharField(max_length=256, blank=False, null=False)

class Comentario(models.Model):
    email = models.CharField(max_length=256, blank=False, null=False)
    especie = models.ForeignKey(Especie)
