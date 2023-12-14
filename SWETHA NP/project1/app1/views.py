from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,'base.html')


def signup(request):
    if request.method=='POST':
        username=request.POST.get('name')
        email=request.POST.get('Email')
        password=request.POST.get('password')
        confirmPassword=request.POST.get('confirmPassword')
        if password==confirmPassword:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username alreadt exists!!!')
                print("already have")
            else:
                new_user=User.objects.create_user(username,email,password)
                new_user.save()
                return redirect(user_login)
        else:
            print('wrong password')
    return render(request,'signup.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(lists)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(user_login)
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect(user_login)
    
        

def lists(request):
    p=User.objects.all()
    return render(request,'lists.html',{'c':p})