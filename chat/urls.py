from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'chat/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': '/'}, name='logout'),
    url(r'^messages/$', views.messages, name='messages'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^(?P<room_id>[0-9]+)/$', views.chatroom, name='chatroom'),
]
