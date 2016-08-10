from django.conf.urls import url, include
from django.contrib import admin
from people.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('tasks.urls')),
<<<<<<< HEAD
    url(r'', include('people.urls', namespace='people')),
   	url(r'^$', index, name='index'),
    url(r'^login$',view_login, name='view_login')
=======
    url(r'', include('activities.urls')),
>>>>>>> 291829a521225903a01c86a1e3aa7cfcd952c5f2
]
