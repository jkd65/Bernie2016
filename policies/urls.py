from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.splash),
	url(r'^policies/$', views.table_of_contents),
	url(r'^policies/(?P<pk>[0-9]+)/$', views.content_detail),
	url(r'^policies/(?P<pk>[0-9]+)/edit/$', views.content_edit, name='content_edit'),
]