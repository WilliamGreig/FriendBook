from django import forms
from .models import *

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'major', 'year']
