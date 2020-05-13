from django.forms import ModelForm
from models import Vendors, Vendorhistory

class vendorForm(ModelForm):
    class Meta:
        model = Vendors
        fields = ['__all__']

class vendorhistoryForm(ModelForm):
    class Meta:
        model = Vendorhistory
        fields = ['__all__']
