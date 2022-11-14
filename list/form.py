from django import forms
from django.forms import SelectDateWidget

from list.models import Task


class TaskForm(forms.ModelForm):
    deadline_time = forms.DateField(widget=SelectDateWidget, required=False)

    class Meta:
        model = Task
        fields = ("description",  "completion", "tags")
