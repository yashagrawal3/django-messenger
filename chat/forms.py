import re
from django import forms
#from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _

class MsgForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ('message', )