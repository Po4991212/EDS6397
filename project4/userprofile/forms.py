from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from .models import Userprofile

class SignUpForm(UserCreationForm):
    street_address = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=100, required=False)
    zipcode = forms.CharField(max_length=10, required=False)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'street_address', 'city', 'state', 'zipcode', 'phone_number')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control'
    }))

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = '__all__'
        exclude = ('user',)
