from django.conf.urls import url, include, patterns
from django.contrib import admin
from people.views import *
from tasks.views import view_index, view_board, add_board_tasks
urlpatterns = [

	url(r'^$', login_required(view_index), name='index'),
	url(r'^board$', view_board, name='board'),
	url(r'^board/addTasks$', add_board_tasks, name='add_board_tasks'),
	url(r'^administrator$', view_administrator, name='administrator'),	
    url(r'^admin/', admin.site.urls),

    url(r'', include('people.urls')),
    url(r'', include('tasks.urls')),    
	url(r'', include('activities.urls')),
	url('', include('social.apps.django_app.urls', namespace='social')),
]
