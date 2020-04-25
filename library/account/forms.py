from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, widget = forms.TextInput())
    password = forms.CharField(widget = forms.PasswordInput())