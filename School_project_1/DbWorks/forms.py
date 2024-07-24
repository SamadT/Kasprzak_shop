from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    email = forms.EmailField(required=True, max_length=100)
    message = forms.CharField(widget=forms.Textarea, max_length=200)