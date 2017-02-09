from django.conf.urls import include, url
from . import views

#url(r'^admin/$', views.admin)

urlpatterns = [	
	url(r'^hira/$', views.hira),
	url(r'^josefina/$', views.josefina)
]