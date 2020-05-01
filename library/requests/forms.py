from django import forms
from .models import ExchangeRequest
class RequestExchangeForm(forms.ModelForm):
    bookTitle = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Book Title'}))
    bookAuthor = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Book Author'}))
    bookState = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=(('DM','DAMAGED'),('US','USED'),('NE','NEW')))
    class Meta:
        model = ExchangeRequest
        fields = ['bookTitle','bookAuthor','bookState','bookImage']