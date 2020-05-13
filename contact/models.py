from django.db import models

# Create your models here.
class Vendors(models.Model):
    vendor = models.CharField(max_length=50)
    vendor_contact = models.CharField(max_length=50)
    vendor_role = models.CharField(max_length=25)
    vendor_address1 = models.CharField(max_length=50)
    vendor_address2 = models.CharField(max_length=50)
    vendor_city = models.CharField(max_length=50)
    vendor_state = models.CharField(max_length=2)
    vendor_zip = models.CharField(max_length=10)
    vendor_phone = models.CharField(max_length=10)
    vendor_ext = models.CharField(max_length=5)
    vendor_entered_by = models.IntegerField(max_length=1)