from __future__ import unicode_literals

from django.db import models

       
class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True)
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField(null=True, blank=True, default="")
    source = models.TextField(null=True, blank=True, default="")
    rating = models.IntegerField(default=1)
    def __str__(self):
        return self.name
 