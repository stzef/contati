from django.conf.urls import url, include
from django.contrib import admin
from people.views import *

urlpatterns = [
   
  
    url(r'^view_login$',view_login, name='view_login'),
   	url(r'^view_register$',view_register, name='view_register'),
   	url(r'^register_user$', register_user, name='register_user'),
   

]
