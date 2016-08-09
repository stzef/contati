from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^tasks$',views.view_tasks, name='view_tasks'),
]
