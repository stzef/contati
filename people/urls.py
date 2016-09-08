from django.conf.urls import url, include, patterns
from django.contrib import admin
from people.views import *
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import login 
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
   
  
   	

   	url(r'^login$', login, {'template_name':'login.html'}, name='login'),
   	url(r'^authenticate$', authenticate, name='authenticate'),
	url(r'^logout$',auth_views.logout, {'next_page':'/'}, name="logout"),
	
	url(r'^view_register$',view_register, name='view-register'),
   	url(r'^register$', register_user, name='register-user'),  	
   	

   	url(r'^profile$', profile,  name='profile'),
	url('^change-password$', change_password, name='change-password'),

	url(r'^customers$', views.list_Customers, name='list_customers'),
	url(r'^customers/add$', views.createCustomers.as_view(), name='add_customers'),
	url(r'^customers/(?P<pk>\d+)/edit/$', views.editCustomers.as_view(), name='edit_customers'),
	url(r'^customers/(?P<pk>\d+)/delete/$', views.deleteCustomers, name='delete_customers'),

	
	
 ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
