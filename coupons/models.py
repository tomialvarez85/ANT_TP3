from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length = 40) 
    discount_percentage = models.PositiveIntegerField()
    currency = models.CharField(max_length = 4)
    
