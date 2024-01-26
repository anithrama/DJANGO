from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('helo welcome')
def index(request):
    return HttpResponse('helo welcome')
def template(request):
    return render(request,'home.html')