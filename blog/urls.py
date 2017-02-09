from django.conf.urls import include, url
from . import views

#url(r'^admin/$', views.admin)

urlpatterns = [	
	url(r'^$', views.post_list),
	url(r'^post_list/$', views.post_list),
	url(r'^post/(?P<id>[0-9]+)/$', views.post_detail),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<id>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]