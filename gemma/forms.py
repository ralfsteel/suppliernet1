from django import forms
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget

from gemma.models import Producers, Pricelist, Promotional, PricelistMain, PromotionalMain


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Producers
        fields = ['email', 'name', 'address', 'zipcode', 'city', 'phone', 'phones', 'fax']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password', 'email']



class PricelistForm(forms.ModelForm):

    class Meta:
        model = Pricelist
        fields = ['pricelist_name', 'pricelist_detail', ]

class PromotionalForm(forms.ModelForm):

    class Meta:
        model = Promotional
        fields = ['promotional_name', 'promotional_detail']

class PricelistMainForm(forms.ModelForm):

    class Meta:
        model = PricelistMain
        fields = ['name']

class PromotionalMainForm(forms.ModelForm):

    class Meta:
        model = PromotionalMain
        fields = ['name']


