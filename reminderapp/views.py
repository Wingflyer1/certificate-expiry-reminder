from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, welcome to the certificate-reminder-app.<br><br>Here we'll develop a cool new and usefull app for people with,<br>a need to keep their papers up to date.")
