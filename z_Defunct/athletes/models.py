from __future__ import unicode_literals

from django.db import models
from datetime import date, datetime

# Create your models here.
POSITIONS= (
    ('P', 'Port'),
    ('S', 'Starboard'),
    ('B', 'Both'),
    ('N', 'None Listed'),
)
OPTIONS= (
    ('Y', 'Yes'),
    ('N', 'No'),
)
TEST_TYPE= (
    ('2', '2k'),
    ('6', '6k'),
    ('3', '30min'),
)
class ErgTest(models.Model):
    name = models.CharField(max_length= 10, choices=TEST_TYPE, default = '2k')
    score = models.CharField(max_length=1, default='00:00.0')  
    
    
class Rower(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True) 
    dob = models.DateField()
    position = models.CharField(max_length=2, choices=POSITIONS, default = 'N')
    scull = models.CharField(max_length=1, choices=OPTIONS, default = 'N')
    erg_scores = models.ManyToManyField(ErgTest, blank=True)
    class Meta:
        permissions = ( 
            ( "read_tests", "Can read test scores" ),
            ( "modify_tests", "Can modify test scores"),
        )
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

class Coxwain(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True) 
    dob = models.DateField()
    weight = models.IntegerField()
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
    
