from django.db import models

# Create your models here.

class CustomerInquiry(models.Model):
    full_name = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=18, blank=True, null=True)
    email = models.EmailField(verbose_name='email address', max_length=100)
    message = models.CharField(max_length=100, blank=True, null=True)
    inquiry_is_processed = models.BooleanField(default=False, verbose_name="Processed")
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="sent on")

    def __str__(self):   
        return self.email