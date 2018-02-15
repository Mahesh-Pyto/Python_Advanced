# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Apps(models.Model):

    Name = models.CharField(max_length=50)
    designer = models.CharField(max_length=50)
    logo = models.ImageField()
    description = models.TextField()


    def __str__(self):
        return self.Name

