from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Room(models.Model):
    room_name = models.CharField(max_length=10, unique=True)
    messages = models.ManyToManyField(User, through='Message')
    def __str__(self):
	return self.room_name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
