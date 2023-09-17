from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):

    return render(request,'AuthenticateApp/index.html')

def register(request):

    return render(request,'AuthenticateApp/register.html')

def my_login(request):

    return render(request,'AuthenticateApp/my-login.html')

def dashboard(request):

    return render(request,'AuthenticateApp/dashboard.html')