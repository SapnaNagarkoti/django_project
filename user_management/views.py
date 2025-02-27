from calendar import firstweekday
from urllib.request import Request

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from user_management.forms import userform
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from.models import customuser
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
    return render(request,'home.html')


def user_register(request):
        if request.method == 'POST':
            data = userform(request.POST,request.FILES)
            password = request.POST['password']
            if data.is_valid():
                user = data.save(commit=False)
                user.username = user.email
                user.set_password(password)
                user.save()
                print(user)
                messages.success(request,'successfully registered')
                return redirect('user_login')
            else:
               messages.error(request,'form data is not valid')
               return redirect('user_register')
        else:
            data = userform(request.POST, request.FILES)
            return render(request,'user-register.html',{'form':data})


def user_login(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('user_list')
            else:
                messages.error(request, "User not found")
                return redirect('user_login')
        else:
            return render(request, 'user-login.html')
    except Exception as e:
        print(e)
        messages.error(request, "An error occurred. Please try again.")
        return redirect('user_login')


@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    messages.success(request,'successfully logout')
    return redirect('user_login')


@login_required(login_url='user_login')
def user_list(request):
    user_data = customuser.objects.filter(is_superuser=False)
    messages.success(request,'user found successfully')
    return render(request,'user-list.html',{'user_data':user_data})


@login_required(login_url='user_login')
def update_user(request,id):
    data = customuser.objects.filter(id=id).first()
    if request.method == 'POST':
        data = userform(request.POST, request.FILES ,instance = data)
        if data.is_valid():
            data.save()
            messages.success(request,'user data updated successfully')
            return redirect('user_list')
        else:
            print("form data is not valid")
    else:
       data = userform(instance=data)
       return render(request, 'user-update.html', {'id':id,'form': data})
    return HttpResponse("not success")


@login_required(login_url='user_login')
def delete_user(request,id):
    user_data = customuser.objects.filter(id=id)
    user_data.delete()
    messages.success(request,'data deleted successfully')
    return redirect(user_list)


def follow_author(request):
    return HttpResponse("follow author function")


def view_profile(request,id):
    user = customuser.objects.filter(id=id).first()
    return render(request,'user-profile.html',{'user':user})

