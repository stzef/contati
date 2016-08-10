from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^tasks$',views.view_tasks, name='view_tasks'),
	url(r'^tasks/<pk>$',views.edit_tasks, name='edit_tasks'),
	url(r'^tasks/add$',views.add_tasks, name='add_tasks'),

	url(r'^states/add$',views.add_states, name='add_states'),
	url(r'^states$',views.list_states, name='list_states'),
	url(r'^states/(?P<pk>\d+)/edit/$', views.edit_states, name='edit_states'),
]

