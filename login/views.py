from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request): 
     return render(request, "login/login.html")

def patientLogin(request):
     return render(request, "login/patientLogin.html")

def staffLogin(request):
     pass

def patientProcess(request):
     pass
