from django.conf.urls import url, include, patterns
patterns
from django.contrib import admin
from people.views import *
from tasks.views import view_index, view_board

urlpatterns = [

	url(r'^$', view_index, name='index'),
	url(r'^board$', view_board, name='board'),
    url(r'^admin/', admin.site.urls),

    url(r'', include('people.urls')),
    url(r'', include('tasks.urls')),    
	url(r'', include('activities.urls')),
]
