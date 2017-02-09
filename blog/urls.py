from django.conf.urls import include, url
from . import views

#url(r'^admin/$', views.admin)

urlpatterns = [	
	url(r'^post_list/$', views.post_list),	
]