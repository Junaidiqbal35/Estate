from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email, RegexValidator

from  .models import Profile
from django.contrib.auth.forms import UserCreationForm
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo','bio', 'phone']

        widgets = {
                    'phone': forms.NumberInput(attrs={

                                                        'class' : 'form-control','input'
                                                         'placeholder': 'Enter your Phone number',
                                                     }),

                    'bio': forms.Textarea(attrs={
                                                        'class': 'input',
                                                        'class': 'form-control',
                                                        'placeholder': ' tell about yourself ',

                                                  })

                    }
class UserRegistrationForm(UserCreationForm):
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphacharacters are allowed.')
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[A-Za-z ]+',
               'title': 'Enter Characters Only '}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[A-Za-z ]+',
               'title': 'Enter Characters Only '}))

    email = forms.EmailField(required=True, label='Email')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]


    def clean_email(self):
        """
        email = self.cleaned_data.get("email")

        if not "gmail.com" in email:
            raise forms.ValidationError("Email should be gmail.com")
        return email
        """
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is not unique")
        return email


    """"
    def clean_email(self):

            # Get the email

        email = self.cleaned_data['email']
        try:
            match = User.objects.get(email=email)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError("  already taken")
        """

    """
        widgets = {
                     'username': forms.TextInput(attrs={
                                                    'class': 'input',
                                                    'class': 'form-control',
                                                    'placeholder': 'Enter unique User Name :',

                                                   }),
                     'first_name': forms.TextInput(attrs={
                                                    'class': 'input',
                                                    'class': 'form-control',
                                                    'placeholder': 'Enter First Name :',

                                                     }),
                     'last_name': forms.TextInput(attrs={
                                                    'class': 'input',
                                                    'class': 'form-control',
                                                    'placeholder': 'Enter last name  :',

                                                     }),
                     'email': forms.EmailField(attrs={
                                                'class': 'input',
                                                'class': 'form-control',


                                            })

                   }
         """
"""
    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        Min_Length = 8
        if password and confirm_password:
            if password != confirm_password:
                raise  forms.ValidationError(" password and confirm password not matched")
            else:
                if len(password) < Min_Length:
                     raise forms.ValidationError("Password  should have atleast 8 character")
        return  confirm_password

    def clean_username(self):
        user = self.cleaned_data['username']
        try:
            match = User.objects.get(username = user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError (" username already taken")


    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            email = validate_email(email)
        except:
            return forms.ValidationError("email is not in correct form")
        return  email



"""


