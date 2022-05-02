from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# main page
def index(request):
    return render(request,'index.html',)


# render to all pages
def welcome(request):
    num_meetings = Meeting.objects.count()
    meetings = Meeting.objects.all()
    return render(request,'website/welcome.html',{'num_meetings':num_meetings, 'meetings':meetings})


def date(request):
    return HttpResponse(f'This page was served at {datetime.now()}')


def about(request):
    return HttpResponse('Hello this is Phone Thiri, rocking with Django!')

# logout user
def logoutuser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')