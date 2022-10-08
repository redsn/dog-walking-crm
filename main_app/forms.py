from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Activity, UserProfile
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ('date', 'activity')

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta: 
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserEditForm(ModelForm):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=10)
    address = forms.CharField(max_length=100)

    class Meta: 
        model = UserProfile
        fields = ('first_name','last_name', 'email', 'phone', 'address') 

class UserProfileForm(ModelForm):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=10)
    address = forms.CharField(max_length=100)

    class Meta:
        model = UserProfile
        fields = ('first_name','last_name', 'email', 'phone', 'address')
