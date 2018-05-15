from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)    
    description = models.CharField(max_length=200)   


    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.name
