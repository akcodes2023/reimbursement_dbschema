from django.shortcuts import render
from django.http import HttpResponse

# import viewsets
from rest_framework import viewsets


# import local data
from .serializers import EmployeeSerializer
from .models import *



# create a viewset 
class EmployeeViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Employee.objects.all()
 
    # specify serializer to be used
    serializer_class = EmployeeSerializer

# Create your views here.

def homepage(request):

    return render(request,'AuthenticateApp/index.html')

def register(request):

    return render(request,'AuthenticateApp/register.html')

def my_login(request):

    return render(request,'AuthenticateApp/my-login.html')

def dashboard(request):

    return render(request,'AuthenticateApp/dashboard.html')