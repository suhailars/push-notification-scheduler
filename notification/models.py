
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=100)
    time_to_send = models.DateTimeField()
    conditional_clause = models.CharField(max_length=30)
    total_number = models.IntegerField(default=0)
    completed_number = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'notifications'