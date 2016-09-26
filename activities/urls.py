from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^activities/$',login_required(views.list_activities), name='list_activities'),#GEt
    url(r'^activities/add/$',login_required(views.add_activity), name='add_activity'),#POST
    url(r'^activities/(?P<pk>\d+)/$',login_required(views.action_activity), name='edit_activity'),#PUT
    url(r'^activities/(?P<pk>\d+)/$',login_required(views.action_activity), name='delete_activity'),#DELETE
    url(r'^projects/$',login_required(views.list_projects), name='list_projects'),#GET
    url(r'^projects/add/$',login_required(views.add_projects), name='add_projects'),#POST
    url(r'^projects/(?P<pk>\d+)/$',login_required(views.action_projects), name='edit_projects'),#PUT
    url(r'^projects/(?P<pk>\d+)/$',login_required(views.action_projects), name='delete_projects'),#DELETE
    url(r'^config/$',login_required(views.list_config), name='list_config'),#GET
    url(r'^reportes/$',login_required(views.list_repotres), name='list_repotres'),#GEt
]