from django.contrib.auth import forms
from django.forms import ModelForm
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

from users.models import *


class CreateUserForm(forms.ModelForm):
    # manager = forms.ModelChoiceField(queryset=Account.objects.filter(Role__startswith='Manager').values('Full_name'))
    # tl_fields = forms.ModelChoiceField(queryset=Account.objects.filter(Role__startswith='TL'))
    class Meta:
        model = UserProfile
        fields =  ['first_name','last_name','email','password']