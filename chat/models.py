from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Room(models.Model):
    room_name = models.CharField(max_length=20, unique=True)
    links = models.ManyToManyField(User, through='Link')
    def __str__(self):
	return self.room_name

@python_2_unicode_compatible
class Link(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    def __str__(self):
	return "%s [%s]" % (self.room.room_name, self.user.username)

class Message(models.Model):
    links = models.ForeignKey(Link, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
