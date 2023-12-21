from django.shortcuts import render
from .models import *
from .form import *

# Create your views here.
def home(request):
    form=bookform()
    if request.method=='POST':
        form=bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return booklist(request)
    return render(request,'index.html',{"form":form})

def booklist(request):
   b=Book.objects.all()
   return render(request,'booklist.html',{'t':b})
   