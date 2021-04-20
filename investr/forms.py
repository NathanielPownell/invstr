from django import forms
from users.models import Position, Wlist

class EnterPositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['user', 'entryprice', 'symbol']

class wlist_form(forms.ModelForm):
    class Meta:
        model = Wlist
        fields = ['user', 'symbol']