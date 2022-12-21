from django.db import models
from django.db.models.fields import Field
from django.forms import ModelForm, fields
from .models import Room
from django.contrib.auth.models import User 

class RommForm(ModelForm):
    class Meta:
        model = Room
        fields= '__all__'
        exlude= ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['username', 'email']   