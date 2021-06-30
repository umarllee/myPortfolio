from django.contrib import admin
from . models import Contact


class contactadmin(admin.ModelAdmin):
    fields= ["name" , "lastname" , "email" , "message"]

admin.site.register(Contact,contactadmin)
