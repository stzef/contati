from django import forms
from .models import States, States_kanban, Priorities, Departments, Tasks
from people.models import Contributors

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

class TasksForm(forms.ModelForm):

    def __init__(self,user, *args, **kwargs):
        super(TasksForm, self).__init__(*args, **kwargs)
        self.fields['responsible'].initial = Contributors.objects.get( user = user )
        self.fields['prioritie'].initial = Priorities.objects.get(name_prioritie= "Media")
        self.fields['states'].initial = States.objects.get(name_states= "Activo")
        self.fields['states_kanban'].initial = States_kanban.objects.get(name_states= "Por hacer")

    class Meta:
        model = Tasks
        fields = {
                'description',
                'answer',
                'responsible',
                'department',
                'prioritie',
                'states',
                'start_date',
                'finish_date',
                'states_kanban',
                'activity',
                'Customers',
        }
        labels = {
                'description' : 'Descripcion',
                'answer' : 'Respuesta',
                'responsible' : 'Responsable' ,
                'department' : 'Departamento' ,
                'prioritie' : 'Prioridad' ,
                'states' : 'Estado',
                'start_date' : 'fecha Inicio',
                'finish_date' : 'fecha Entrega',
                'states_kanban' : 'Estado Kanban',
                'activity' : 'Actividad',
                'Customers' : 'Cliente',
        }
        widgets = {
                'responsible' : forms.Select(attrs={'class':'form-control', 'value': '{{ object.responsible }}' }) ,
                'description' : forms.Textarea(attrs={'class':'form-control'}),
                'answer' : forms.Textarea(attrs={'class':'form-control'}),
                'department' : forms.Select(attrs={'class':'form-control'}) ,
                'prioritie' : forms.Select(attrs={'class':'form-control'}) ,
                'states' : forms.Select(attrs={'class':'form-control'}), 
                'start_date' : forms.TextInput(attrs={'class':'form-control','type':'date','min':'1980-01-01','max':'2025-12-31'}),
                'finish_date' : forms.TextInput(attrs={'class':'form-control','type':'date','min':'1980-01-01','max':'2025-12-31'}),
                'states_kanban' : forms.Select(attrs={'class':'form-control'}),
                'activity' : forms.Select(attrs={'class':'form-control', 'id':'id_activi', 'value' : '{{ object.activity }}' }),
                'Customers' : forms.Select(attrs={'class':'form-control'}),
        }        