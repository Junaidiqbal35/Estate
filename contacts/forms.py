from django import forms
from django.forms import Textarea

from .models import Contact


class ReplyMesaageForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['message',]
        widgets = {
            'message': Textarea(attrs={
                'class': 'input',
                'class': 'form-control',
                'placeholder': ' Enter Message Here !!',
                'cols': 100, 'rows': 5}),
        }
