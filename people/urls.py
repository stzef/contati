from django.conf.urls import url, include, patterns
from django.contrib import admin
from people.views import *
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import login 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
  
   	url(r'^view_register$',view_register, name='view-register'),
   	url(r'^register$', register, name='register-user'),  	
   	url(r'^authenticate$', authenticate, name='authenticate'),

   	url(r'^login$', login, {'template_name':'login.html'}, name='login'),
	url(r'^logout$',auth_views.logout, {'next_page':'/'}, name="logout"),
	url(r'^logon$', logon, name='logon'),

   	url(r'^profile$', profile, name='profile'),
	url(r'^profile/change-password$', view_change_password, name='view-change-password'),
	url('^change-password$', change_password, name='change-password'),

	
 ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
