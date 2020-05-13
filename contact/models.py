from django.db import models

# Create your models here.
class Vendors(models.Model):
    vendor_id = models.AutoField(db_column='Vendor_ID', primary_key=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor_contact = models.CharField(db_column='Vendor_Contact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor_role = models.CharField(db_column='Vendor_Role', max_length=25, blank=True, null=True)  # Field name made lowercase.
    vendor_address = models.CharField(db_column='Vendor_Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor_email = models.CharField(db_column='Vendor_Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor_city = models.CharField(db_column='Vendor_City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor_state = models.CharField(db_column='Vendor_State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    vendor_zip = models.CharField(db_column='Vendor_Zip', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vendor_phone = models.CharField(db_column='Vendor_Phone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vendor_ext = models.CharField(db_column='Vendor_Ext', max_length=5, blank=True, null=True)  # Field name made lowercase.
    vendor_entered_by = models.SmallIntegerField(db_column='Vendor_Entered_By')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vendors'

    def __str__(self):
        return self.vendor


class Vendorhistory(models.Model):
    vendorhistory_id = models.AutoField(db_column='VendorHistory_ID', primary_key=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor_contact = models.CharField(db_column='Vendor_Contact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor_role = models.CharField(db_column='Vendor_Role', max_length=25, blank=True, null=True)  # Field name made lowercase.
    vendor_address = models.CharField(db_column='Vendor_Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor_email = models.CharField(db_column='Vendor_Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor_city = models.CharField(db_column='Vendor_City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor_state = models.CharField(db_column='Vendor_State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    vendor_zip = models.CharField(db_column='Vendor_Zip', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vendor_phone = models.CharField(db_column='Vendor_Phone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vendor_ext = models.CharField(db_column='Vendor_Ext', max_length=5, blank=True, null=True)  # Field name made lowercase.
    vendor_change_code = models.CharField(db_column='Vendor_Change_Code', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vendor_change_record = models.CharField(db_column='Vendor_Change_Record', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vendor_change_dt = models.DateTimeField(db_column='Vendor_Change_DT', blank=True, null=True)  # Field name made lowercase.
    vendor_change_by = models.SmallIntegerField(db_column='Vendor_Change_By')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VendorHistory'

    def __str__(self):
        return self.vendor

