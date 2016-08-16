from django.conf.urls import url, include
from django.contrib import admin
from people.views import *
from django.contrib.auth import views as auth_views 

urlpatterns = [
   
  
    url(r'^login$',view_login, name='view-login'),
    url(r'^logon$', logon, name='logon'),
   	url(r'^register$',view_register, name='view-register'),
   	url(r'^$', register, name='register-user'),
   	url(r'^authenticate$', authenticate, name='authenticate'),
   	url(r'^logout$',auth_views.logout, {'next_page':'/'}, name="logout"),
   	url(r'^profile$', profile, name='profile'),
   	url(r'^profile/change-password$', view_change_password, name='view-change-password'),
   	url(r'^profile/change-password$', change_password, name='change-password')

]