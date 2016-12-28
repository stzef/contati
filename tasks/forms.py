from django import forms
from .models import States, States_kanban, Priorities, Departments, Tasks, Color, Answer
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
        fields = ['name_states']
        labels = {'name_states': 'Nombre Estado'}
        widgets = {'name_states': forms.TextInput(attrs={'class':'form-control'})}

class ColorForm(forms.ModelForm):

    class Meta:
        model = Color
        fields = ['name_color', 'hexadecimal']
        labels = {'name_color': 'Color', 'hexadecimal': 'Hexadecimal'}
        widgets = {'name_color': forms.TextInput(attrs={'class':'form-control'}),
                    'hexadecimal': forms.TextInput(attrs={'class':'form-control'})
                  }

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
                'name_task',
                'description',

                'responsible',
                'department',
                'prioritie',
                'states',
                'estimated_time',
                'total_time',
                'states_kanban',
                'activity',
                'Customers',
        }
        labels = {
                'name_task': 'Nombre de la Tarea',
                'description' : 'Descripcion',

                'responsible' : 'Responsable' ,
                'department' : 'Departamento' ,
                'prioritie' : 'Prioridad' ,
                'states' : 'Estado',
                'estimated_time' : 'Hora Estimada',
                'total_time' : 'Hora Real',
                'states_kanban' : 'Estado Kanban',
                'activity' : 'Actividad',
                'Customers' : 'Cliente',
        }
        widgets = {
                'name_task': forms.TextInput(attrs={'class':'form-control'}),
                'responsible' : forms.Select(attrs={'class':'form-control', 'value': '{{ object.responsible }}', 'name':'responsible' }) ,
                'description' : forms.Textarea(attrs={'class':'form-control', 'id':'description', 'name':'description', 'filas':'4', 'cols':'50'}),

                'department' : forms.Select(attrs={'class':'form-control', 'name':'department'}) ,
                'prioritie' : forms.Select(attrs={'class':'form-control', 'name':'prioritie'}) ,
                'states' : forms.Select(attrs={'class':'form-control', 'name':'states'}),
                'estimated_time' : forms.TextInput(attrs={'name':'estimated_time', 'class':'form-control'}),
                'total_time' : forms.TextInput(attrs={'name':'total_time', 'class':'form-control'}),
                'states_kanban' : forms.Select(attrs={'class':'form-control', 'name':'states_kanban'}),
                'activity' : forms.Select(attrs={'name':'activity', 'class':'form-control', 'id':'id_activi', 'value' : '{{ object.activity }}' }),
                'Customers' : forms.Select(attrs={'name':'customers', 'class':'form-control'}),
        }

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('description',)
        labels = {'description':'Comentario'}
        widgets = { 'description': forms.Textarea(attrs={'class':'form-control'})}
