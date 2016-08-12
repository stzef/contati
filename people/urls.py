from django.conf.urls import url, include
from django.contrib import admin
from people.views import *
from django.contrib.auth import views as auth_views 

urlpatterns = [
   
  
    url(r'^login$',view_login, name='view_login'),
    url(r'^logon$', logon, name='logon'),
   	url(r'^register$',view_register, name='view_register'),
   	url(r'^$', register, name='register_user'),
   	url(r'^authentication$', authentication, name='authentication'),
   	url(r'^logout$',auth_views.logout, {'next_page':'/'}, name="logout"),
   	url(r'^profile$', profile, name='profile')
]