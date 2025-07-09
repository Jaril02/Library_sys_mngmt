from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Book,Member,Issue

@login_required
def home(request):
    return render(request,'library_app/home.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password')
    return render(request,'library_app/login.html')


def user_logout(request):
    logout(request)
    messages.success(request,"You have succesfully loged out")
    return  redirect('user_login')

@login_required
def book_list(request):
    books=Book.objects.all()
    return render(request,'library_app/book_list.html',{'books':books})

# Create your views here.
