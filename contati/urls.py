from django.conf.urls import url, include, patterns
from django.contrib import admin
from people.views import *
from tasks.views import view_index, view_board, view_boardx4, view_boardx5, edit_board, tareas_index
from django.contrib.auth.decorators import login_required
urlpatterns = [

    url(r'^tasks_project/(?P<pk>\d+)/$', tasks_project, name='tasks_project'),

	url(r'^$', login_required(view_index), name='index'),
	url(r'^tareas_index/(?P<pk>\d+)/$',tareas_index, name='tareas_index'),
	url(r'^board$', view_board, name='board'),
    url(r'^boardx4$', view_boardx4, name='boardx4'),
    url(r'^boardx5$', view_boardx5, name='boardx5'),
	url(r'^board/(?P<pk>\d+)/edit/$', edit_board , name='edit_board_tasks'),

	url(r'^administrator$', login_required(view_administrator.as_view()), name='administrator'),
    url(r'^administrator$', login_required(proyect.as_view()), name='proyect'),
    url(r'^admin/', admin.site.urls),

    url(r'^tasks-ad$', tasks, name='tasks_ad'),


    url(r'^tasks-ad/add$', login_required(tasks_add.as_view()), name='tasks_add'),
    url(r'^tasks_list$', login_required(tasks_list.as_view()), name='tasks_list'),
    url(r'^tasks-ad/edit/(?P<pk>\d+)/$', login_required(tasks_edit.as_view()), name='tasks_edit'),
    url(r'^tasks-ad/delete(?P<pk>\d+)/$', login_required(tasks_delete.as_view()), name='tasks_delete'),

    url(r'^departments_add$', login_required(departments_add.as_view()), name='departments_add'),
    #url(r'^departments_list$', login_required(departments_list.as_view()), name='departments_list'),
    url(r'^departments_list$', departments_list, name='departments_list'),
    url(r'^departments/edit/(?P<pk>\d+)/$', login_required(departments_edit.as_view()), name='departments_edit'),
    url(r'^departments/delete(?P<pk>\d+)/$', login_required(departments_delete.as_view()), name='departments_delete'),

    url(r'^states_kanban$', states_kanban_list, name='states_kanban_list'),
    url(r'^states_kanban/add$', login_required(StatesKanbanCreate.as_view()), name='states_kanban_add'),
    url(r'^states_kanban/edit/(?P<pk>\d+)/$', login_required(StatesKanbanEdit.as_view()), name='states_kanban_edit'),
    url(r'^states_kanban/delete/(?P<pk>\d+)/$', login_required(StatesKanbanDelete.as_view()), name='states_kanban_delete'),

    url(r'^states_add$',states_add, name='states_add'),
    url(r'^states_list$',states_list, name='states_list'),
    url(r'^states-ad/edit/(?P<pk>\d+)/$',login_required(States_edit.as_view()), name='states_edit'),
    url(r'^states-ad/delete/(?P<pk>\d+)/$',login_required(States_delete.as_view()), name='states_delete'),

    url(r'^priorities_list$', priorities_list, name='priorities_list'),
    url(r'^priorities_add$', login_required(Priorities_create.as_view()), name='priorities_add'),
    url(r'^priorities-ad/edit/(?P<pk>\d+)/$', login_required(Priorities_edit.as_view()), name='priorities_edit'),
    url(r'^priorities-ad/delete/(?P<pk>\d+)/$', login_required(Priorities_delete.as_view()), name='priorities_delete'),

    url(r'^activities_list$',login_required(activities_list), name='activities_list'),#GEt
    url(r'^activities_add/$',login_required(activity_add), name='activity_add'),#POST
    url(r'^activities-ad/edit/(?P<pk>\d+)/$',login_required(Activity_edit.as_view()), name='activity_edit'),#PUT
    url(r'^activities-ad/delete/(?P<pk>\d+)/$',login_required(activity_delete), name='activity_delete'),#DELETE

    url(r'^customers_list$', login_required(Customers_list), name='customers_list'),
    url(r'^customers-ad/add/$', login_required(Customers_add.as_view()), name="customers_add"),
    url(r'^customers-ad/edit/(?P<pk>\d+)/$', login_required(Customers_edit.as_view()), name="customers_edit"),
    url(r'^customers-ad/delete/(?P<pk>\d+)/$', login_required(Customers_delete.as_view()), name="customers_delete"),

    url(r'^projects_list$',login_required(projects_list), name='projects_list'),#GET
    url(r'^projects_add/$',login_required(projects_add), name='projects_add'),#POST
    url(r'^projects-ad/edit/(?P<pk>\d+)/$',login_required(Projects_edit.as_view()), name='projects_edit'),#PUT
    url(r'^projects-ad/delete/(?P<pk>\d+)/$',login_required(projects_delete), name='projects_delete'),#DELETE

    url(r'^reports$',login_required(reports), name='reports'),
    url(r'^configuration$',login_required(configuration), name='configuration'),

    url(r'', include('people.urls')),
    url(r'', include('tasks.urls')),
	url(r'', include('activities.urls')),

]
