from django import forms

class ContactForm(forms.Form):
    email_Address = forms.EmailField(
        label=(""),
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email Address...',
                'class': 'common-input mt-20'
            }),
        required=True
    )
    name = forms.CharField(
        label=(""),
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Preferred Name...',
                'class': 'common-input mt-20',
    }))

    message = forms.CharField(
        label=(""),
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Message...',
                'class': 'common-input mt-20',
                'rows':'4'
            }),
        required=True
    )

