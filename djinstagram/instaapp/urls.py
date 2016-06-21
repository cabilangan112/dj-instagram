from django.conf.urls import url

from . import views

app_name = 'instaapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^upload/$', views.upload_photo, name='upload_photo'),
    url(r'^users/$', views.users, name='users'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^follow/$', views.follow_user, name='follow_user'),
    url(r'^following/$', views.user_following, name='user_following'),
    url(r'^followers/$', views.user_followers, name='user_followers'),
    url(r'^feed/$', views.feed, name='feed'),
]
