from django.urls import path
from . import views

urlpatterns = [
    path('network/', views.network, name='app-network'),
    path('servers/', views.servers, name='app-servers'),
    path('workstations/', views.workstations, name='app-workstations'),
]