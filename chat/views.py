from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .models import *

def index(request):
    user_list = User.objects.all()
    context = {
        'user_list' : user_list,
    }
    return render(request, 'chat/index.html', context)

def messages(request):
    chats = Message.objects.filter(user=request.user)
    context = {
	'chats' : chats,
    }
    return render(request,'chat/messages.html',context)

def chatroom(request,room_id):
    users = Message.objects.filter(room_id=room_id)
    room = Room.objects.get(pk=room_id)
    context = {
        'users' : users,
	'room' : room,
    }
    return render(request, 'chat/room.html', context)
'''
def chatroom(request, label):
    room, created = Room.objects.get_or_create(label=label)

    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "chat/room.html", {
        'room': room,
        'messages': messages,
    })
'''
