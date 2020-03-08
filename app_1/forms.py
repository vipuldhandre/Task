from .models import *
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username',] # 'password']


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
