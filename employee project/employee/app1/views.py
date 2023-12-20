from django.shortcuts import render
from .models import *
from .form import Emform
# Create your views here.
def add(request):
    d=Emform()
    if request.method=="POST":
        d=Emform(request.POST)
        if d.is_valid():
            d.save()
            return home(request)
    return render(request,'add.html',{'q':d})
def home(request):
    p=Employee.objects.all()
    return render(request,'lists.html',{'z':p})