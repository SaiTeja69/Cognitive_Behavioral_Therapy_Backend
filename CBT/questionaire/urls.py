  
from django.conf.urls import url
from . import views

urlpatterns = [
	# /DynamicQ/
    url(r'^survey', views.survey, name='survey'),

	# /DynamicQ/1
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name ='detail'),
	
	
]