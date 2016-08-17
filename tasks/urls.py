from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^tasks$',views.view_tasks, name='view_tasks'),
	url(r'^tasks/<pk>$',views.edit_tasks, name='edit_tasks'),
	url(r'^tasks/add$',views.add_tasks, name='add_tasks'),

	url(r'^states/add$',views.add_states, name='add_states'),
	url(r'^states$',views.list_states, name='list_states'),
	url(r'^states/(?P<pk>\d+)/edit/$', views.editStates.as_view(), name='edit_states'),
	url(r'^states/(?P<pk>\d+)/delete/$', views.deleteStates.as_view(), name='delete_states'),

	url(r'^states-kanban$', views.list_states_kanban, name='list_states_kanban'),
	url(r'^states-kanban/add$', views.createStatesKanban.as_view(), name='add_states_kanban'),
	url(r'^states-kanban/(?P<pk>\d+)/edit/$', views.editStatesKanban.as_view(), name='edit_states_kanban'),
	url(r'^states-kanban/(?P<pk>\d+)/delete/$', views.deleteStatesKanban.as_view(), name='delete_states_kanban'),
]

