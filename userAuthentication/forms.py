from django import forms
from django.forms import Textarea
from django.contrib.auth.models import User
from .models import UserInfo
from django.utils.translation import gettext_lazy as _


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email')


class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('gender', 'facebook_id', 'profile_image')

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = UserInfo
        fields  = ('profile_image',)
        labels = {
            'profile_image': _(''),
        }
        # widgets = {
        #     'profile_image': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }
        # field_classes = {
        #     'profile_image': MySlugFormField,
        # }

