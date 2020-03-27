from django import forms
from django.forms import Textarea
from .models import Appointment

class CreateAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('title', 'start', 'end', 'description')
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
