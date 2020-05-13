from django.shortcuts import render
from contact.models import Vendors, Vendorhistory

# Create your views here.
def contact(request):
    vendors = Vendors.objects.all()
    return render(request, 'contact/index.html', {"vendors": vendors})