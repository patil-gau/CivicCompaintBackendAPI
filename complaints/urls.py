from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('allcomplaints/', views.AllComplaints),
    path('addcomplaint/',views.AddComplaint,name="add_complaint"),
    path('admin/home/',views.AdminHome,name="admin_home"),
    path('officer/home/<id>/',views.OfficerHome,name="officer_home"),
    path('latestcomplaints/',views.LatestComplaints,name="latest_complaints"),
    path('latestcomplaints/<int:pk>',views.LatestComplaintsCitizen,name="latest_complaints"),
    path('allcomplaints/officer/<id>/',views.AllOfficerComplaints,name="total_officer_complaints"),
    path('pending/complaints/',views.PendingComplaints,name="pending_complaints"),
    path('pending/complaints/<int:pk>',views.PendingComplaintsOfficer,name="pending_complaints_officer"),
    path('resolved/complaints/',views.ResolvedComplaints,name="resolved_complaints"),
    path('delete/<comp_id>/',views.DeleteComplaints,name="delete_complaints"),
    path('updatecomplaint/',views.UpdateComplaints,name="update_complaints"),
    path('resolvedcompla/complaints/pending/complaints/6ints/<int:pk>',views.ResolvedComplaintsOfficer,name="update_complaints")


]

