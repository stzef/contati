from django.conf.urls import url, include, patterns
from django.contrib import admin
from people.views import *
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import login 
from people.views import Register_user

urlpatterns = [
   
  	
    
    url(r'^profile$', profile, name='profile'),
    url(r'^logon$', logon, name='logon'),

   	url(r'^view_register$',view_register, name='view-register'),
   	# url(r'^$', register, name='register-user'),
   	url(r'^register$',Register_user.as_view(), name='register-user'),   	
   	url(r'^authenticate$', authenticate, name='authenticate'),

   	url(r'^logout$',auth_views.logout, {'next_page':'/'}, name="logout"),
#    	url(r'^profile/change-password$', view_change_password, name='view-change-password'),
#    	url(r'^profile/change-password$', change_password, name='change-password')
	url(r'^login$', login, {'template_name':'login.html'}, name='login'),


 ]