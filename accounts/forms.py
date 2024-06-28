from django import forms
from . models import User

class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password','profile')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email Address'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Password'}),
            'profile': forms.FileInput(attrs={'class': 'form-control'}),
        }