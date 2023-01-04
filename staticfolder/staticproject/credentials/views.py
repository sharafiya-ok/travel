from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect


# Create your views here.
def login (request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request.user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')


    return render(request,"login.html")
def register(request):
    if request.method =='post':
        user_name=request.POST['user_name']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword= request.POST['confirm_password']

        if password==cpassword:
            if User.objects.filter(user_name=user_name).exists():
                messages.info(request,"username taken")
                return redirect ('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect ('register')
            else:
                user=User.object.create_user(user_name=user_name,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"incorrect password")
            return redirect('register')
            return redirect('/')

    return render(request,"register.html")
def logout (request):
    auth.logut(request)
    return render('/')
