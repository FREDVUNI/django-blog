from django.db import models

class Blogger(models.Model):
    title = models.CharField(max_length = 30)
    slug  =  models.SlugField(unique=True)
    details = models.TextField(null=True,blank=True) 