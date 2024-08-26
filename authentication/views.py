from django.shortcuts import render
from django.http import HttpResponse
from . import views

# Create your views here.
def home(request):
    return HttpResponse(request, "authentication/index.html")

def signup(request):
    return render(request, "authentication/signup.html")

def signin(request):
    return render(request, "authentication/signin.html")

def signout(request):
    pass