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
    room_list = Room.objects.all()
    context = {
    'user_list' : user_list,
    'room_list' : room_list,
    }
    return render(request, 'chat/index.html', context)
