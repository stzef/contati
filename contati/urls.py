from django.conf.urls import url, include, patterns
from django.contrib import admin
from people.views import *
from tasks.views import view_index, view_board, createTasksBoard
from django.contrib.auth.decorators import login_required
urlpatterns = [

	url(r'^$', login_required(view_index), name='index'),
	url(r'^board$', view_board, name='board'),
	url(r'^board/addTasks$', login_required(createTasksBoard.as_view()), name='add_board_tasks'),
	url(r'^administrator$', view_administrator, name='administrator'),	
    url(r'^admin/', admin.site.urls),

    url(r'', include('people.urls')),
    url(r'', include('tasks.urls')),    
	url(r'', include('activities.urls')),
	
]
