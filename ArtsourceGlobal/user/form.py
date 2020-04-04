from django import forms
from captcha.fields import CaptchaField
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import LazyTypedChoiceField
from django_countries import countries

gender_choices = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='password', max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='captcha')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=128, label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=256, label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=256, label='Confirm password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    realName = forms.CharField(max_length=128, label='Your real name', required=False)

    # referee = forms.CharField(max_length=128, label='Referee\'s name',
    #                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    refEmail = forms.EmailField(label='Referee\'s Email', required=False,
                                widget=forms.EmailInput(attrs={'class': 'form-control'}))
    country = LazyTypedChoiceField(choices=countries, label='Country', required=False)
    # artist = forms.ChoiceField(choices=artist_choices, label='artist')
    captcha = CaptchaField(label="Captcha")
    gender = forms.ChoiceField(choices=gender_choices, label='Gender', required=False)
    age = forms.IntegerField(max_value=150, min_value=0, label='Age', required=False)
    street1 = forms.CharField(max_length=512, label='Street1', required=False)
    street2 = forms.CharField(max_length=512, label='Street2', required=False)
    suburb = forms.CharField(max_length=128, label='Suburb', required=False)
    state = forms.CharField(max_length=128, label='State', required=False)
    postalCode = forms.CharField(max_length=128, label='Postal Code', required=False)
    phone = forms.CharField(max_length=24, label='Phone number', required=False)


class ProfileForm(forms.Form):
    username = forms.CharField(max_length=128, label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = LazyTypedChoiceField(choices=countries, label='Country', required=False)
    gender = forms.ChoiceField(choices=gender_choices, label='Gender', required=False)
    age = forms.IntegerField(max_value=150, min_value=0, label='Age', required=False)
    street1 = forms.CharField(max_length=512, label='Street1', required=False)
    street2 = forms.CharField(max_length=512, label='Street2', required=False)
    suburb = forms.CharField(max_length=128, label='Suburb', required=False)
    state = forms.CharField(max_length=128, label='State', required=False)
    postalCode = forms.CharField(max_length=128, label='Postal Code', required=False)
    phone = forms.CharField(max_length=24, label='Phone number', required=False)

    painting = forms.BooleanField(label='painting', required=False,
                                  widget=forms.CheckboxInput(attrs={'class': 'form-interest'}))
    sculpture = forms.BooleanField(label='sculpture', required=False,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-interest'}))
    photography = forms.BooleanField(label='photography', required=False,
                                     widget=forms.CheckboxInput(attrs={'class': 'form-interest'}))
    calligraphy = forms.BooleanField(label='calligraphy', required=False,
                                     widget=forms.CheckboxInput(attrs={'class': 'form-interest'}))
    printmaking = forms.BooleanField(label='printmaking', required=False,
                                     widget=forms.CheckboxInput(attrs={'class': 'form-interest'}))
    art_and_craft = forms.BooleanField(label='art_and_craft', required=False,
                                       widget=forms.CheckboxInput(attrs={'class': 'form-interest'}))
    seal_cutting = forms.BooleanField(label='seal_cutting', required=False,
                                      widget=forms.CheckboxInput(attrs={'class': 'form-interest'}))
    art_design = forms.BooleanField(label='art_design', required=False,
                                    widget=forms.CheckboxInput(attrs={'class': 'form-interest'}))
