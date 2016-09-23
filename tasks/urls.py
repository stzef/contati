from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^tasks$',views.list_tasks, name='list_tasks'),
	url(r'^tasks/<pk>$',views.editTasks.as_view(), name='edit_tasks'),
	url(r'^tasks/add$',views.createTasks.as_view(), name='add_tasks'),

	url(r'^states/add$',views.add_states, name='add_states'),
	url(r'^states$',views.list_states, name='list_states'),
	url(r'^states/(?P<pk>\d+)/$', views.editStates.as_view(), name='edit_states'),
	url(r'^states/(?P<pk>\d+)/delete/$', views.deleteStates.as_view(), name='delete_states'),

	url(r'^states-kanban$', views.list_states_kanban, name='list_states_kanban'),
	url(r'^states-kanban/add$', views.createStatesKanban.as_view(), name='add_states_kanban'),
	url(r'^states-kanban/(?P<pk>\d+)/edit/$', views.editStatesKanban.as_view(), name='edit_states_kanban'),
	url(r'^states-kanban/(?P<pk>\d+)/delete/$', views.deleteStatesKanban.as_view(), name='delete_states_kanban'),

	url(r'^priorities$', views.list_priorities, name='list_priorities'),
	url(r'^priorities/add$', views.createPriorities.as_view(), name='add_priorities'),
	url(r'^priorities/(?P<pk>\d+)/edit/$', views.editPriorities.as_view(), name='edit_priorities'),
	url(r'^priorities/(?P<pk>\d+)/delete/$', views.deletePriorities.as_view(), name='delete_priorities'),

	url(r'^departments$', views.list_departments, name='list_departments'),
	url(r'^departments/add$', views.createDepartments.as_view(), name='add_departments'),
	url(r'^departments/(?P<pk>\d+)/edit/$', views.editDepartments.as_view(), name='edit_departments'),
	url(r'^departments/(?P<pk>\d+)/delete/$', views.deleteDepartments.as_view(), name='delete_departments'),


]

