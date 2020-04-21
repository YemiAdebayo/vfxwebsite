from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=18, blank=True, null=True)
    email = models.EmailField(verbose_name='email address', max_length=100)
    course = models.CharField(max_length=100, blank=True, null=True)
    registration_is_processed = models.BooleanField(default=False, verbose_name="Processed")
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="registered on")

    def __str__(self):   
        return self.email
