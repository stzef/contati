from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url('^activities$',views.list_activities, name='list_activities'),#GEt
    url('^activities/add',views.add_activity, name='add_activity'),#POST
    url('^activities/<pk>',views.action_activity, name='edit_activity'),#PUT
    url('^activities/<pk>',views.action_activity, name='delete_activity'),#DELETE
    url('^products',views.list_products, name='list_products'),#GET
    url('^products/add',views.add_product, name='add_product'),#POST
    url('^products/<pk>',views.action_product, name='edit_product'),#PUT
    url('^products/<pk>',views.action_product, name='delete_product'),#DELETE
]