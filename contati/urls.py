from django.conf.urls import url, include, patterns
patterns
from django.contrib import admin
from people.views import *
from tasks.views import view_index

urlpatterns = [

	url(r'^$', view_index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'', include('people.urls')),
    url(r'', include('tasks.urls')),    
	url(r'', include('activities.urls')),
]
