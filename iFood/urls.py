from django.conf.urls import url
from iFood import views


app_name = 'iFood'


urlpatterns = [ 
	url(r'^$', views.index, name='index'),
	url(r'about/$', views.about, name='about'),
]
