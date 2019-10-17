from django import forms
from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profession', 'bio', 'location', 'birth_date', 'skils', 'education', 'edu_center', 'linkedin_profile', 'facebook_profile', 'twitter_profile', 'birth_date', 'image')

class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model= User
        fields = ('first_name', 'last_name', 'email', 'password')
        labels ={
           'first_name': 'First Name',
           'last_name': 'Last Name',
           'email': 'Your email',
        }

class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Field('username', css_class='input-sm'),
        Field('email', css_class='input-sm'),
        Field('first_name', css_class='input-sm'),
        Field('last_name', css_class='input-sm'),
        FormActions(Submit('Update', 'Update', css_class='btn-primary'))
    )
 
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(UpdateProfile, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        labels ={
           'username': 'Your username',
           'first_name': 'First Name',
           'last_name': 'Last Name',
           'email': 'Your email',
           'password1': 'Your password',
           'password2': 'Please confirm your password'

        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['first_name']
        user.email = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user