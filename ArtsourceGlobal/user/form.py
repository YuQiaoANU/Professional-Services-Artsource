from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='password', max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='captcha')


class RegisterForm(forms.Form):
    # artist_choices = (
    #     ('Yes', 'Yes'),
    #     ('No', 'No'),
    # )

    username = forms.CharField(max_length=128, label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=256, label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=256, label='Confirm password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    realName = forms.CharField(max_length=128, label='Your real name',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    # referee = forms.CharField(max_length=128, label='Referee\'s name',
    #                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    refEmail = forms.EmailField(label='Referee\'s Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    # artist = forms.ChoiceField(choices=artist_choices, label='artist')
    captcha = CaptchaField(label="Captcha")
