from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('users/', views.QUserView.as_view()),
	url(r'^login/$', views.RegisterFormView.as_view())
]
