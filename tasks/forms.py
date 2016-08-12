from django import forms
from .models import States

class StatesForm(forms.ModelForm):

    class Meta:
        model = States
        fields = ['name_states']
        labels = {'name_states': 'states_name'}
        widgets = {'name_states': forms.TextInput(attrs={'class':'forms-control'})}