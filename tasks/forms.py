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

    def __init__(self,user=None, *args, **kwargs):
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
                'start_date' : 'Hora Estimada',
                'finish_date' : 'Hora Total',
                'states_kanban' : 'Estado Kanban',
                'activity' : 'Actividad',
                'Customers' : 'Cliente',
        }
        widgets = {
                'responsible' : forms.Select(attrs={'class':'form-control', 'value': '{{ object.responsible }}', 'name':'responsible' }) ,
                'description' : forms.Textarea(attrs={'class':'form-control', 'id':'demos', 'name':'description'}),
                'answer' : forms.Textarea(attrs={'class':'form-control', 'name':'answer'}),
                'department' : forms.Select(attrs={'class':'form-control', 'name':'department'}) ,
                'prioritie' : forms.Select(attrs={'class':'form-control', 'name':'prioritie'}) ,
                'states' : forms.Select(attrs={'class':'form-control', 'name':'states'}),
                'start_date' : forms.TextInput(attrs={'name':'start_date', 'class':'form-control','type':'time'}),
                'finish_date' : forms.TextInput(attrs={'name':'finish_date', 'class':'form-control','type':'time'}),
                'states_kanban' : forms.Select(attrs={'class':'form-control', 'name':'states_kanban'}),
                'activity' : forms.Select(attrs={'name':'activity', 'class':'form-control', 'id':'id_activi', 'value' : '{{ object.activity }}' }),
                'Customers' : forms.Select(attrs={'name':'customers', 'class':'form-control'}),
        }
