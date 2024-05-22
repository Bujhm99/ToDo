from django import forms

from todo.models import Task


class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"


class DateTimeLocalField(forms.DateTimeField):
    input_formats = [
        "%Y-%m-%dT%H:%M",
    ]
    widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M")


class TaskForm(forms.ModelForm):
    deadline = DateTimeLocalField()

    class Meta:
        model = Task
        fields = "__all__"
