from django import forms
from .models import States, States_kanban, Priorities, Departments

class StatesForm(forms.ModelForm):

    class Meta:
        model = States
        fields = ['name_states']
        labels = {'name_states': 'Nombre Estado'}
        widgets = {'name_states': forms.TextInput(attrs={'class':'form-control'})}

class StatesKanbanForm(forms.ModelForm):

    class Meta:
        model = States_kanban
        fields = ['name_states', 'color']
        labels = {'name_states': 'Nombre Estado',
                   'color' : 'Color'}
        widgets = {'name_states': forms.TextInput(attrs={'class':'form-control'}),
                    'color' : forms.TextInput(attrs={'class':'form-control'})}  

class PrioritiesForm(forms.ModelForm):

    class Meta:
        model = Priorities
        fields = ['name_prioritie', 'order']
        labels = {'name_prioritie': 'Nombre Prioridad',
                   'order' : 'Orden'}
        widgets = {'name_prioritie': forms.TextInput(attrs={'class':'form-control'}),
                    'order' : forms.TextInput(attrs={'class':'form-control'})}  

class DepartmentsForm(forms.ModelForm):

    class Meta:
        model = Departments
        fields = ['name_department']
        labels = {'name_department': 'Nombre Departamento'}
        widgets = {'name_department': forms.TextInput(attrs={'class':'form-control'})}