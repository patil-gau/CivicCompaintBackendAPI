from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ComplaintSerializer
from .models import Complaints
from rest_framework.response import Response
from users.models import Users
from state_city.models import Cities
from django.http import HttpResponseBadRequest

# Create your views here.

@api_view(['GET'])
def AllComplaints(request):
    if request.method == 'GET':
        complaints = Complaints.objects.all()
        serializer = ComplaintSerializer(complaints,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def AdminHome(request):
    if request.method == 'GET':
      try:
        total_users = Users.objects.count()
        total_officers = Users.objects.filter(role='officer').count()
        total_issues = Complaints.objects.all().count()
        total_issues_pending = Complaints.objects.filter(progress__lt = 100).count()
        total_issues_resolved = Complaints.objects.filter(progress=100).count()
        total_cities = Cities.objects.all().count()
        jsonResponse = {
         "total_users":total_users,
         "total_officers":total_officers,
         "total_complaints":total_issues,
         "total_complaints_pending":total_issues_pending,
         "total_complaints_resolved":total_issues_resolved,
         "total_cities":total_cities 
        }
        return Response(jsonResponse)
      
      except Exception as e:
        jsonResponse = {
         "total_users":"",
         "total_officers":"",
         "total_complaints":"",
         "total_complaints_pending":"",
         "total_complaints_resolved":"",
         "total_cities":"" 
        }
        print(e)
        return Response()    
    
    return HttpResponseBadRequest    

@api_view(['POST'])
def AddComplaint(request):
    if request.method == 'POST':
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response({"Message":"Your Complaint is registered successfully"})
        else:
          return Response(serializer.errors)  

    return HttpResponseBadRequest()
