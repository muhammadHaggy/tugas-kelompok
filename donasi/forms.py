from django import forms

class Pembayaran(forms.Form):
    nominal = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'id':'input-nominal'}))
    