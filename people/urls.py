from django.conf.urls import url, include, patterns
from django.contrib import admin
from people.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from . import views





urlpatterns = [




   	url(r'^login/$', login, {'template_name':'login.html'}, name='login'),
   	url(r'^authenticate$', authenticate, name='authenticate'),
	url(r'^logout$',auth_views.logout, {'next_page':'login'}, name="logout"),


	url(r'^view_register$',view_register, name='view-register'),
   	url(r'^register$', register_user, name='register-user'),
   	

   	url(r'^profile$', profile,  name='profile'),
	url('^change-password$', views.change_password, name='change-password'),
	url('^change-image$', views.change_image, name='change-image'),

	url(r'^customers/$', login_required(views.list_Customers), name='list_customers'),
	#url(r'^customers/add/$', add_Customers, name="add_customers"),
	url(r'^customers/add/$', login_required(views.createCustomers.as_view()), name="add_customers"),
	url(r'^customers/(?P<pk>\d+)/edit/$', login_required(views.editCustomers.as_view()), name="edit_customers"),
	url(r'^customers/(?P<pk>\d+)/delete$', login_required(views.deleteCustomers.as_view()), name='delete_customers'),



 ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
