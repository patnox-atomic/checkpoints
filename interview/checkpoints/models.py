##Patnox 27-07-2021

import datetime
from django.db import models
from django.utils import timezone

class CheckedPoints(models.Model):
    query = models.CharField(max_length=200)
    response = models.CharField(max_length=200)
    check_date = models.DateTimeField(auto_now_add=True)
    ##check_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.query


