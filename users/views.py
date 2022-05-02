from django.shortcuts import render
from users.forms import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate

from django.http import request, HttpResponse

from users.models import *

# Create your views here.

# user register page
def registerpage(request):
    try:
        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            email = request.POST.get('email')
            lastname = request.POST.get('lastname')
            password = request.POST.get('passwd')
            UserProfile(first_name=firstname, last_name=lastname, email=email, password=password).save()

            messages.sucess(request, "Check Your Login Details")
            return render(request, 'login.html')
        else:
            return render(request, 'index.html')
    except:
        messages.error(request, "Check Your Login Details")
        return render(request, 'index.html')


# user login page
def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('lpassword')
        if UserProfile.objects.filter(email=email, password=password).exists():

            return redirect('welcome')
        else:
            return redirect('/')



    #
    #     user = authenticate(request, username=username, password=password)
    #
    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)
    #             if user.Role == "Manager":
    #                 return redirect('manager')
