
from django import forms
from .models import *

class UserForm(forms.ModelForm):

    class Meta:
        model = user
        widgets = {
        'user_password':forms.PasswordInput(),
        }
        fields = ['user_name','user_email','user_password','user_age','user_adhaar','user_blood','user_phone','user_area','user_city','user_pin']


class DonorForm(forms.ModelForm):

    class Meta:
        model = donor
        fields = ['donor_organ','donor_blood','donor_kidney','donor_heart','donor_lung','donor_eye']


class NeederForm(forms.ModelForm):

    class Meta:
        model = needer
        fields = ['needer_organ','needer_blood','needer_kidney','needer_heart','needer_lung','needer_eye','needer_area','needer_city','needer_pin']

class EmerForm(forms.ModelForm):

    class Meta:
        model = emergency
        fields = ['emer_blood','emer_area','emer_city','emer_pin']


class LoginForm(forms.ModelForm):

    class Meta:
        model = user
        widgets = {
            'user_password' : forms.PasswordInput(),
        }
        fields = ['user_email','user_password']
