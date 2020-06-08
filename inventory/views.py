from django.shortcuts import render

# Create your views here.
def network(request):
    return render(request, 'inventory/index1.html', {})

def servers(request):
    return render(request, 'inventory/index2.html', {})

def workstations(request):
    return render(request, 'inventory/index3.html', {})