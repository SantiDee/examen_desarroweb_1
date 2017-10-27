# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

# Create your models here.
class car(models.Model):
    # relacionar al usuario
    make = models.CharField(max_length=140)
    Type = models.CharField(max_length=140)
    year = models.CharField(max_length=140)
    colour = models.CharField(max_length=140)
    price  = models.DecimalField(max_digits=9999, decimal_places=2)
    
def _str_(sefl):
    return str_(self.make)
