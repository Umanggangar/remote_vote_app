from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('vote_candidate', views.vote_candidate, name='vote_candidate'),
	path('vote', views.vote, name='vote'),
	path('thanks', views.thanks, name='thanks'),
	path('new_user', views.new_user, name='new_user'),	
]
