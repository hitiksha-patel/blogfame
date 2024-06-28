from django import forms
from . models import Blog
from accounts.models import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields  = '__all__'
        exclude = ('user',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Blog Title'}),
            'blog_type': forms.Select(attrs={'class': 'form-dropdown'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Description...'}),
            'picture': forms.FileInput(attrs={'class': 'form-control',}),
        }

class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields  = '__all__'
        exclude = ('user',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'blog_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email','profile')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email Address'}),
            'profile': forms.FileInput(attrs={'class': 'form-control'}),
        }