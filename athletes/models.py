from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Rower(models.Model):
    first_name = models.CharField(
        verbose_name = 'first', 
        max_length=20, 
        null=True,
        blank=False
    )
    last_name = models.CharField(
        verbose_name = 'last', 
        max_length=30, 
        null=True,
        blank=False
    )
    middle_initial = models.CharField(
        verbose_name = 'initial', 
        max_length=1, 
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return str(self.last_name) + ', ' + str(self.first_name)
    