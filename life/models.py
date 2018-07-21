from django.db import models

class Recipe(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  
  
class Steps(models.Model):
  stepOne = models.CharField(max_length=100)
  stepTwo = models.CharField(max_length=100)
  stepThree = models.CharField(max_length=100)
  
  recipeKey = models.ForeignKey(Recipe, on_delete=models.CASCADE)