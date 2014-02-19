from django import forms
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget

from gemma.models import Producers, Pricelist


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Producers
        fields = ['name', 'password', 'address', 'zipcode', 'city', 'phone', 'phones', 'fax', 'email']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'password']

class PricelistForm(forms.ModelForm):

    class Meta:
        model = Pricelist
        fields = ['pricelist_name', 'pricelist_detail']




