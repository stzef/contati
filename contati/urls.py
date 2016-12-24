from django.conf.urls import url, include, patterns
from django.contrib import admin
from people.views import *
from tasks.views import view_index, view_board, view_boardx4, view_boardx5, edit_board, tareas_index, tasks_project, edit_states_kanban
from django.contrib.auth.decorators import login_required
urlpatterns = [

    #url(r'^tasks_project/(?P<pk>\d+)/$', tasks_project, name='tasks_project'),


	url(r'^$', login_required(view_index), name='index'),
    url(r'^admin/index$', index_admin, name='index_admin'),

	url(r'^tareas_index/(?P<pk>\d+)/$',tareas_index, name='tareas_index'),
	url(r'^board$', view_board, name='board'),
    url(r'^boardx4$', view_boardx4, name='boardx4'),
    url(r'^boardx5$', view_boardx5, name='boardx5'),
	url(r'^board/(?P<pk>\d+)/edit/$', edit_board , name='edit_board_tasks'),
	url(r'^board/(?P<pk>\d+)/kanban/$', edit_states_kanban , name='edit_states_kanban'),

    url(r'^admin/$', view_administrator, name='administrator'),
    #url(r'^admin$', login_required(view_administrator.as_view()), name='administrator'),
    url(r'^admin/tasks_responsible/(?P<pk>\d+)/$', tasks_responsible, name='tasks_responsible'),
    url(r'^admin/', admin.site.urls),

    url(r'^admin/tasks-ad/(?P<pk>\d+)/$', tasks_ad, name='tasks_ad'),

    url(r'^admin/tasks_project/(?P<pk>\d+)/$', tasks_project, name='tasks_project'),

    url(r'^admin/profile$', profile_admin,  name='profile_admin'),
    url('^admin/change-password$', change_password_admin, name='change-password_admin'),
    url('^admin/change-image$', change_image_admin, name='change-image_admin'),

    url(r'^admin/tasks-ad/add$', login_required(tasks_add.as_view()), name='tasks_add'),
    url(r'^admin/tasks_list$', login_required(tasks_list.as_view()), name='tasks_list'),
    url(r'^admin/tasks-ad/edit/(?P<pk>\d+)/$', login_required(tasks_edit.as_view()), name='tasks_edit'),
    url(r'^admin/tasks-ad/delete(?P<pk>\d+)/$', login_required(tasks_delete.as_view()), name='tasks_delete'),

    url(r'^admin/departments_add$', login_required(departments_add.as_view()), name='departments_add'),
    #url(r'^departments_list$', login_required(departments_list.as_view()), name='departments_list'),
    url(r'^admin/departments_list$', departments_list, name='departments_list'),
    url(r'^admin/departments/edit/(?P<pk>\d+)/$', login_required(departments_edit.as_view()), name='departments_edit'),
    url(r'^admin/departments/delete(?P<pk>\d+)/$', login_required(departments_delete.as_view()), name='departments_delete'),

    url(r'^admin/states_kanban$', states_kanban_list, name='states_kanban_list'),
    url(r'^admin/states_kanban/add$', login_required(StatesKanbanCreate.as_view()), name='states_kanban_add'),
    url(r'^admin/states_kanban/edit/(?P<pk>\d+)/$', login_required(StatesKanbanEdit.as_view()), name='states_kanban_edit'),
    url(r'^states_kanban/delete/(?P<pk>\d+)/$', login_required(StatesKanbanDelete.as_view()), name='states_kanban_delete'),

    url(r'^admin/states_add$',states_add, name='states_add'),
    url(r'^admin/states_list$',states_list, name='states_list'),
    url(r'^admin/states-ad/edit/(?P<pk>\d+)/$',login_required(States_edit.as_view()), name='states_edit'),
    url(r'^admin/states-ad/delete/(?P<pk>\d+)/$',login_required(States_delete.as_view()), name='states_delete'),

    url(r'^admin/priorities_list$', priorities_list, name='priorities_list'),
    url(r'^admin/priorities_add$', login_required(Priorities_create.as_view()), name='priorities_add'),
    url(r'^admin/priorities-ad/edit/(?P<pk>\d+)/$', login_required(Priorities_edit.as_view()), name='priorities_edit'),
    url(r'^admin/priorities-ad/delete/(?P<pk>\d+)/$', login_required(Priorities_delete.as_view()), name='priorities_delete'),

    url(r'^admin/activities_list$',login_required(activities_list), name='activities_list'),#GEt
    url(r'^admin/activities_add/$',login_required(activity_add), name='activity_add'),#POST
    url(r'^admin/activities-ad/edit/(?P<pk>\d+)/$',login_required(Activity_edit.as_view()), name='activity_edit'),#PUT
    url(r'^admin/activities-ad/delete/(?P<pk>\d+)/$',login_required(activity_delete), name='activity_delete'),#DELETE

    url(r'^admin/customers_list$', login_required(Customers_list), name='customers_list'),
    url(r'^admin/customers-ad/add/$', login_required(Customers_add.as_view()), name="customers_add"),
    url(r'^admin/customers-ad/edit/(?P<pk>\d+)/$', login_required(Customers_edit.as_view()), name="customers_edit"),
    url(r'^admin/customers-ad/delete/(?P<pk>\d+)/$', login_required(Customers_delete.as_view()), name="customers_delete"),

    url(r'^admin/projects_list$',login_required(projects_list), name='projects_list'),#GET
    url(r'^admin/projects_add/$',login_required(projects_add), name='projects_add'),#POST
    url(r'^admin/projects-ad/edit/(?P<pk>\d+)/$',login_required(Projects_edit.as_view()), name='projects_edit'),#PUT
    url(r'^admin/projects-ad/delete/(?P<pk>\d+)/$',login_required(projects_delete), name='projects_delete'),#DELETE

    url(r'^admin/reports$',login_required(reports), name='reports'),
    url(r'^admin/configuration$',login_required(configuration), name='configuration'),
    
    url(r'', include('people.urls')),
    url(r'', include('tasks.urls')),
	url(r'', include('activities.urls')),

]
