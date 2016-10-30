from django.conf.urls import url, include, patterns
from django.contrib import admin
from people.views import *
from tasks.views import view_index, view_board
from django.contrib.auth.decorators import login_required
urlpatterns = [

	url(r'^$', login_required(view_index), name='index'),
	url(r'^board$', view_board, name='board'),
	# url(r'^board/addTasks$', login_required(createTasksBoard.as_view()), name='add_board_tasks'),
	url(r'^administrator$', login_required(view_administrator.as_view()), name='administrator'),	
    url(r'^administrator$', login_required(proyect.as_view()), name='proyect'),
    url(r'^admin/', admin.site.urls),
    url(r'^tasks-ad$', tasks, name='tasks_ad'),
    url(r'^tasks/add$', login_required(tasks_add.as_view()), name='tasks_add'),
    url(r'^tasks_list$', login_required(tasks_list.as_view()), name='tasks_list'),
    url(r'^tasks/(?P<pk>\d+)/edit/$', login_required(tasks_edit.as_view()), name='tasks_edit'),
    url(r'^tasks/(?P<pk>\d+)/delete/$', login_required(tasks_delete.as_view()), name='tasks_delete'),
    
    url(r'', include('people.urls')),
    url(r'', include('tasks.urls')),    
	url(r'', include('activities.urls')),
	
]
