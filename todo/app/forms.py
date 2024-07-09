

from django import forms
from .models import Task, Member, Organization

from django import forms
from .models import Task, Member, Organization
from datetime import datetime, timedelta

from django import forms
from .models import Task, Member, Organization
from tempus_dominus.widgets import DateTimePicker

# forms.py

from django import forms
from .models import Task
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
# forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M:%S'],
        widget=DateTimePickerInput(
            options={
                'format': 'YYYY-MM-DD HH:mm:ss',
                'showClear': True,
                'showTodayButton': True,
                'showClose': True,
                'icons': {
                    'time': 'fa fa-clock-o',
                    'date': 'fa fa-calendar',
                    'up': 'fa fa-chevron-up',
                    'down': 'fa fa-chevron-down',
                    'previous': 'fa fa-chevron-left',
                    'next': 'fa fa-chevron-right',
                    'today': 'fa fa-crosshairs',
                    'clear': 'fa fa-trash',
                    'close': 'fa fa-times'
                }
            }
        ),
        required=False
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'member', 'organization']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'member': forms.Select(attrs={'class': 'form-control'}),
            'organization': forms.Select(attrs={'class': 'form-control'}),
        }


class TeamForm(forms.Form):
    name = forms.CharField(max_length=100)
    members = forms.CharField(widget=forms.Textarea)
