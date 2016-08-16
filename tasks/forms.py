from django import forms
from .models import States, States_kanban

class StatesForm(forms.ModelForm):

    class Meta:
        model = States
        fields = ['name_states']
        labels = {'name_states': 'Nombre Estado'}
        widgets = {'name_states': forms.TextInput(attrs={'class':'forms-control'})}

class StatesKanbanForm(forms.ModelForm):

    class Meta:
        model = States_kanban
        fields = ['name_states']
        labels = {'name_states': 'Nombre Estado Color'}
        widgets = {'name_states': forms.TextInput(attrs={'class':'forms-control'})}        