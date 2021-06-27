from django.shortcuts import render
from django.core.mail import send_mail
from projectportfolio import settings
from django.http import HttpResponse
from .models import filedownload

def index(request): 
    return  render( request,'index.html' )

def skills(request): 
    return  render( request,'My_Skills.html')

def works(request): 
    return  render( request,'My_Works.html')

def about(request): 
    return  render( request,'About_Me.html')

def onlinecv(request): 
    return  render( request,'My_Cv.html')


              # Next:  WORKS Page
    
def filmdizi(request): 
    return  render( request,'Film_dizi.html')

def form(request): 
    return  render( request,'Employee_Form.html')


def photography(request): 
    return  render( request,'photography.html')


#in Employee interest form:

def signin(request): 
    return  render( request,'SignIn.html')

def signup(request): 
    return  render( request,'SignUp.html')