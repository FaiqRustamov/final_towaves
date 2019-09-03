from django import forms
from .models import Event, Contactuser
from django.contrib.auth.models import User
from django.contrib.admin import widgets   
from django.utils import timezone
from django.db import models
                             
class ContactForm(forms.Form):
    class Meta:
        model = Contactuser
        fields = ['contact_name','contact_surname','contact_email', 'contact_subject','content']
    
    contact_name = forms.CharField(required=True, widget = forms.TextInput(attrs={'placeholder': 'Name'}))
    contact_surname = forms.CharField(required=True, widget = forms.TextInput(attrs={'placeholder': 'Surname'}))
    contact_email = forms.EmailField(required=True, widget = forms.TextInput(attrs={'placeholder': 'Email'}))
    contact_subject = forms.CharField(required=True, widget = forms.TextInput(attrs={'placeholder': 'Subject'}))
    content = forms.CharField(required=True, widget = forms.TextInput(attrs={'placeholder': 'Message'}))
    


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Enter password'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Enter password again'}))
    
    class Meta:
        model = User
        fields = {
            'username',
            'first_name', 
            'last_name',  
            'email',
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password

from django.forms.widgets import DateTimeInput

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name','description','img', 'start_time','category','appointment_time']
        widgets = {
            'appointment_time': DateTimeInput(attrs={'type': 'date'}),
            'start_time': DateTimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'type': 'text'})
        }