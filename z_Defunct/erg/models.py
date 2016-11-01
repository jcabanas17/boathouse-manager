from __future__ import unicode_literals

from django.db import models
from datetime import date, datetime
from athletes.models import Rower, Coxwain
import re

TEST_TYPE= (
    ('2', '2k'),
    ('6', '6k'),
    ('3', '30min'),
)

# Create your models here.
class ErgScore(models.Model):
    time = models.CharField(max_length=7, default='00:00.0')
    #name = models.ForeignKey(Rower, null=True, unique=True)
    #def __str__(self): 
    #        return self.name
        
class ErgTest(models.Model):
    test_type = models.CharField(max_length= 10, choices=TEST_TYPE, default = '2k')
    date = models.DateField()
    #scores = models.ManyToManyField(ErgScore)
    
