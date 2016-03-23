from django.db import models
import time
from django.core.validators import RegexValidator

import random
from random import randint

owner = models.ForeignKey('auth.User', related_name='register')
highlighted = models.TextField()

class Set_feedback(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=100, blank=True,default='')
    
    class Meta:
        ordering = ('created',)

