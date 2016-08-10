from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^activities$',views.list_activities, name='list-activities'),#GEt
   # url('^activities/add',add_activity, name='add-activity'),#POST
    #url('^activities/<pk>',edit_activity, name='edit-activity'),#PUT
    #rl('^activities/<pk>',delete_activity, name='delete-activity'),#DELETE
    #url('^products',list_products, name='list-products'),#GET
    #url('^products/add',add_product, name='add-product'),#POST
    #url('^products/<pk>',edit_product, name='edit-product'),#PUT
    #url('^products/<pk>',delete_product, name='delete-product'),#DELETE
]
