from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^activities/$',views.list_activities, name='list_activities'),#GEt
    url(r'^activities/add/$',views.add_activity, name='add_activity'),#POST
    url(r'^activities/(?P<pk>\d+)/$',views.action_activity, name='edit_activity'),#PUT
    url(r'^activities/(?P<pk>\d+)/$',views.action_activity, name='delete_activity'),#DELETE
    url(r'^products/$',views.list_products, name='list_products'),#GET
    url(r'^products/add/$',views.add_products, name='add_products'),#POST
    url(r'^products/(?P<pk>\d+)/$',views.action_product, name='edit_product'),#PUT
    url(r'^products/(?P<pk>\d+)/$',views.action_product, name='delete_product'),#DELETE
]