"""projectportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from page import views
from Contact.views import ContactView
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('skills/', views.skills, name="skills"),
    path('works/', views.works, name="works"),
    path('about/', views.about, name="about"),
    path('cv/', views.onlinecv, name="onlinecv"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('film/', views.filmdizi, name="film"),
    path('form/', views.form, name="form"),
    path('photography/', views.photography, name="photography"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
]
 