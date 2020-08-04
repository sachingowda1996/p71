from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def trail(request):
    return HttpResponse("<h1>project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp/home.html")

def profile(request):
    name="sachin"
    return render(request,"myapp/profile.html",{'name':name})            