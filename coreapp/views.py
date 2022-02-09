from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def Devapplyleav(request):
    return render(request,'Devapplyleav.html')
def Devapplyleav1(request):
    return render(request,'Devapplyleav1.html')
def Devapplyleav2(request):
    return render(request,'Devapplyleav2.html')
def Devleaverequiest(request):
    return render(request,'Devleaverequiest.html')
def Devattendance(request):
    return render(request,'Devattendance.html')
def Tattend(request):
    return render(request,'Tattend.html')
def Devapplyleav3(request):
    return render(request,'Devapplyleav3.html')
def Manager_index(request):
    return render(request,'Manager_index.html')
def Manager_accepted_projects(request):
    return render(request,'Manager_accepted_projects.html')
def Manager_rejected_projects(request):
    return render(request,'Manager_rejected_projects.html')





