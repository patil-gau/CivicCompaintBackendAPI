from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('allcomplaints/', views.AllComplaints),
    path('addcomplaint/',views.AddComplaint,name="add_complaint"),
    path('admin/home/',views.AdminHome,name="admin_home")
    
]

