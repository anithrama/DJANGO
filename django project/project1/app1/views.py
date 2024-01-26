from django.shortcuts import render

# Create your views here.
def home(request):
    d={'name':'achu','age':'20'}
    return render(request,'base.html',{'data':d})

def index(request):
    return render(request,'index.html')
