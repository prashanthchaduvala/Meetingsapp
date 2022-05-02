# Project Name :: Meetings

# Commands 
Project creation
- django-admin startproject "Meetings"
- django-admin startapp "Teams"
- django-admin startapp "users"
- django-admin startapp "meetings"

# DataBase
creatinng tables & cloums use below commands, (adding single or more fields into the model use, "migrate command")
- after defining db Schema (models)
- python manage.py makemigrations
- python manage.py migrate

# Installations
install any Third party library (1) or avialable req list use (2) below commands
- pip install packagename
- pip list


# Settings.py
add third party librarys ,apps  and Database changes,,,,,,
>DB settings

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'meetings',  
        'USER':'',  
        'PASSWORD':'',  
        'HOST':'',  
        'PORT':''  
    }  
}  

 ![Example screenshot](imgage/db.png)

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Run Server](#RunServer-Commands)
* [Usage](#usage)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Git Commands](#gitcommands)
* [Host](#host)

## General Information
- This is a Meetings Application.
> What is the purpose of your project?
- working some domain and doing the work as per requirements. 



## Technologies Used
- Django -3.2.8
- djangorestframework -3.12.4
- python -3.6

## Features
List the ready features here:
- Meetings 1
- Developing Videoscreen record


## Screenshots
![Example screenshot]
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
What are the project requirements/dependencies? Where are they listed?
- check A requirements.txt.
- Where is it located? project or git

>Proceed to describe how to install 
clone project
- setup one's local environment 
- get started with the project.


## RunServer-Commands
How to run server  use below commands
- python manage.py runserver 
> below command you can use custom port 
> Feature it will change
- python manage.py runserver 9000


## Project Status
Project is: _in progress


To do:
- Devellope more fields
- Feature to be added 2


## Acknowledgements
- This project was based on Teams Meeting.

## gitcommands
Basic commands
- git clone "clone project url"
- git commit -m "add comments"
- git push 
> creating new branch
- git checkout -b "create your own branch"
- git checkout "branch name"  , switch to another branch


## Host
Moving to production

Before hosting things need to be ensure in settings.py


1.Need add to live port number 
   => ALLOWED_HOSTS = []



3. Need change local DB connections  to DB server connections - add DB name, Port number , Password.
   
>DB postgresql
 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '#',
            'USER': '#',
            'PASSWORD': '#',
            'HOST': '#',
            'PORT': '5432',
    
            }
        }

4. Add all the requirements to requirements.txt without missing any requirement & Need to install all dependencies available in requrements.txt.


5. Run these commands  

    -python manage.py makemigrations
    
    -python manage.py migrate
        
        To generate tables to which DB it is connected

6.Run below command to run the appalication.
    
     -python manage.py runserver 




