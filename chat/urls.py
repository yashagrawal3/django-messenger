from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^messages/$', views.messages, name='messages'),
    url(r'^(?P<room_id>[0-9]+)/$', views.chatroom, name='chatroom'),
]
