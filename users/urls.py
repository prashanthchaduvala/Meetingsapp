from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path,include
from users import views

urlpatterns = [
    ######## User login and register urls###################
    path('register/', views.registerpage, name="register"),
    path('login/', views.loginpage, name='login'),

    # path('logout/', views.logoutuser, name="logout"),

    ]