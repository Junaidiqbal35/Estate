from django import forms
from django.forms import Textarea



from .models import Listing , Comment


class addSpaceForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ['title', 'address','city','state','zipcode','description','wifi','price','bedrooms','bathrooms','garage', 'sqft','lot_size','rules','attendies','photo_main','photo_1','photo_2','photo_3',]

        widgets = {
            'title' : forms.TextInput(attrs={
                                            'class' : 'input',
                                            'class': 'form-control',
                                            'placeholder': 'Wedding Destination , PhotoShoot, Birthday Parties ...e.g....',
                                             }),
            'address' : forms.TextInput(attrs={
                                                'class': 'input',
                                                'class': 'form-control',
                                                 'placeholder': 'Street Address ...',

                                               }),
            'city': forms.TextInput(attrs={
                                                'class': 'input',
                                                'class': 'form-control',
                                                'placeholder': 'Lahore , Sialkot e.g...',

                                              }),
            'state': forms.TextInput(attrs={
                                             'class': 'input',
                                              'class': 'form-control',
                                              'placeholder': 'Punjab, Sindh... e.g...',

                                            }),

            'zipcode': forms.NumberInput(attrs={
                                            'class': 'input',
                                            'class': 'form-control',
                                            'placeholder': '45710, 67690',

                                           }),
            'description': forms.Textarea(attrs={
                                                'class': 'input',
                                                'class': 'form-control',
                                                'placeholder': ' Tell About The Space in Detail, Speciality of your Space e.g.. ',

                                                }),
            'rules': forms.Textarea(attrs={
                                            'class': 'input',
                                            'class': 'form-control',
                                            'placeholder': ' Rules of Space , e.g',

                                        }),

            'price': forms.NumberInput(attrs={
                                                'class': 'input',
                                                'class': 'form-control',
                                                'placeholder': ' Space Price Per Hour',

                                            }),
            'sqft': forms.NumberInput(attrs={
                                            'class': 'input',
                                            'class': 'form-control',
                                            'placeholder': ' 1200 sqft, 100 seft e.g... ',


            }),
            'lot_size': forms.NumberInput(attrs={
                                            'class': 'input',
                                            'class': 'form-control',
                                            'placeholder': ' 1200 lot_size, 100 lot_size e.g... ',

                                        }),
            'attendies': forms.NumberInput(attrs={
                                            'class': 'input',
                                            'class': 'form-control',
                                            'placeholder': 'Max Member handle by your Space...',

            }),
            'garage': forms.NumberInput(attrs={
                                                'class': 'input',
                                                'class': 'form-control',
                                                'placeholder': ' Garage for parking ... ',

                                            }),
            'bathrooms': forms.NumberInput(attrs={
                                                 'class': 'input',
                                                 'class': 'form-control',
                                                  'placeholder': ' Number of washrooms  ... ',

                                                }),
            'bedrooms': forms.NumberInput(attrs={
                                                    'class': 'input',
                                                    'class': 'form-control',
                                                    'placeholder': ' Number of Bedrooms  ... ',

                                                }),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
        widgets = {
            'content': Textarea(attrs={
                'class' : 'input',
                'class' : 'form-control',
                'placeholder': ' Enter comment here !!',
                'cols': 100, 'rows': 5}),

        }



class EditListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'address', 'city', 'state', 'zipcode', 'description', 'wifi', 'price', 'bedrooms',
                  'bathrooms', 'garage', 'sqft', 'lot_size', 'rules', 'attendies', 'photo_main', 'photo_1', 'photo_2',
                  'photo_3', 'photo_4', 'photo_5', 'photo_6']





