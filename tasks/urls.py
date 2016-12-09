from django.conf.urls import include, url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^tasks$',views.list_tasks, name='list_tasks'),
	url(r'^tasks/add$',login_required(views.createTasks.as_view()), name='add_tasks'),
	url(r'^tasks/(?P<pk>\d+)/edit/$',login_required(views.editTasks.as_view()), name='edit_tasks'),
	url(r'^tasks/(?P<pk>\d+)/delete/$',login_required(views.deleteTasks.as_view()), name='delete_tasks'),


	url(r'^states/add$',views.add_states, name='add_states'),
	url(r'^states$',views.list_states, name='list_states'),
	url(r'^states/(?P<pk>\d+)/edit$',login_required(views.editStates.as_view()), name='edit_states'),
	url(r'^states/(?P<pk>\d+)/delete/$',login_required(views.deleteStates.as_view()), name='delete_states'),

	url(r'^states-kanban$', views.list_states_kanban, name='list_states_kanban'),
	url(r'^states-kanban/add$', login_required(views.createStatesKanban.as_view()), name='add_states_kanban'),
	url(r'^states-kanban/(?P<pk>\d+)/edit/$', login_required(views.editStatesKanban.as_view()), name='edit_states_kanban'),
	url(r'^states-kanban/(?P<pk>\d+)/delete/$', login_required(views.deleteStatesKanban.as_view()), name='delete_states_kanban'),

	url(r'^priorities$', views.list_priorities, name='list_priorities'),
	url(r'^priorities/add$', login_required(views.createPriorities.as_view()), name='add_priorities'),
	url(r'^priorities/(?P<pk>\d+)/edit/$', login_required(views.editPriorities.as_view()), name='edit_priorities'),
	url(r'^priorities/(?P<pk>\d+)/delete/$', login_required(views.deletePriorities.as_view()), name='delete_priorities'),

	url(r'^departments$', views.list_departments, name='list_departments'),
	url(r'^departments/add$', login_required(views.createDepartments.as_view()), name='add_departments'),
	url(r'^departments/(?P<pk>\d+)/edit/$', login_required(views.editDepartments.as_view()), name='edit_departments'),
	url(r'^departments/(?P<pk>\d+)/delete/$', login_required(views.deleteDepartments.as_view()), name='delete_departments'),

	url(r'^color$', views.list_color, name='list_color'),
	url(r'^color/add$', login_required(views.createColor.as_view()), name='add_color'),
	url(r'^color/(?P<pk>\d+)/edit/$', login_required(views.editColor.as_view()), name='edit_color'),
	url(r'^color/(?P<pk>\d+)/delete/$', login_required(views.deleteColor.as_view()), name='delete_color'),


	url(r'^generaActividad/(?P<pk>\d+)/$', views.generaActividad, name='generaActividad'),
    url(r'^view_task_board/(?P<pk>\d+)/$', views.view_task_board, name='view_task_board'),

    url(r'^save_task/$', views.save_task, name='save_task'),

]
