from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^activities/$',views.list_activities, name='list_activities'),#GEt
    url(r'^activities/add/$',views.add_activity, name='add_activity'),#POST
    url(r'^activities/(?P<pk>\d+)/$',views.action_activity, name='edit_activity'),#PUT
    url(r'^activities/(?P<pk>\d+)/$',views.action_activity, name='delete_activity'),#DELETE
    url(r'^projects/$',views.list_projects, name='list_projects'),#GET
    url(r'^projects/add/$',views.add_projects, name='add_projects'),#POST
    url(r'^projects/(?P<pk>\d+)/$',views.action_projects, name='edit_projects'),#PUT
    url(r'^projects/(?P<pk>\d+)/$',views.action_projects, name='delete_projects'),#DELETE
    url(r'^config/$',views.list_config, name='list_config'),#GET
]