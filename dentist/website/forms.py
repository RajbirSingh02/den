from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Appointment


class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ['name', 'phone', 'email', 'address', 'schedule', 'date', 'message']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
