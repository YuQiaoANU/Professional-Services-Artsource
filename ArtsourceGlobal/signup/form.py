from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from homepage.models import Artwork, Booking




class SignupForm(UserCreationForm):

    email = forms.CharField(max_length=200, help_text='Required')
    first_name = forms.CharField(max_length=50, help_text='Required')
    last_name = forms.CharField(max_length=50, help_text='Required')
    occupation = forms.CharField()

    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name', 'occupation', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.occupation = self.cleaned_data['occupation']

        if commit:
            user.save()

        return user


