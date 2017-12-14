from __future__ import unicode_literals

from django.db import models

# Create your models here.
class info(models.Model):
    ip = models.CharField(max_length=20)

