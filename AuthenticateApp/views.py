from django.shortcuts import render
from django.http import HttpResponse

"""
# import viewsets
# from rest_framework import viewsets
# import local data
"""

from rest_framework.decorators import api_view, authentication_classes, permission_classes
#, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeSerializer
from .models import *


"""
# create a viewset 
class EmployeeViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Employee.objects.all()
 
    # specify serializer to be used
    serializer_class = EmployeeSerializer
"""

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_employee(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_employee(request):
    
    if request.method == 'POST':
        '''
        # print(type(request.data))
        '''
        # Handle POST request to create a new employee
        serializer = EmployeeSerializer(data=request.data)
        '''
        # print(type(serializer))
        # print(serializer.initial_data)
        '''
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # 201 Created
        return Response(serializer.errors, status=400)  # 400 Bad Request


# Create your views here.

def homepage(request):

    return render(request,'AuthenticateApp/index.html')

def register(request):

    return render(request,'AuthenticateApp/register.html')

def my_login(request):

    return render(request,'AuthenticateApp/my-login.html')

def dashboard(request):

    return render(request,'AuthenticateApp/dashboard.html')