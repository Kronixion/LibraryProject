from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'id':'login','class':'fadeIn first', 'placeholder':'username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'id':'password','class':'fadeIn second','placeholder':'password'}))