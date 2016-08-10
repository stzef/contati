from django import forms
from .models import States

class StatesForm(forms.ModelForm):

    class Meta:
        model = States
        fields = ('name_states')