from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^activities$',views.list_activities, name='list-activities'),#GEt
    url('^activities/add',views.add_activity, name='add-activity'),#POST
    url('^activities/<pk>',views.edit_activity, name='edit-activity'),#PUT
    url('^activities/<pk>',views.delete_activity, name='delete-activity'),#DELETE
    url('^products',views.list_products, name='list-products'),#GET
    url('^products/add',views.add_product, name='add-product'),#POST
    url('^products/<pk>',views.edit_product, name='edit-product'),#PUT
    url('^products/<pk>',views.delete_product, name='delete-product'),#DELETE
]
