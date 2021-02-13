from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    username=forms.CharField(label='Username')
    password1=forms.CharField(widget=forms.PasswordInput(),label='Password')
    password2=forms.CharField(widget=forms.PasswordInput(),label='Password Confirmation')
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

