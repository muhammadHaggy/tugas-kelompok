from django import forms

class ContactForm(forms.Form) :
    name = forms.CharField(max_length=200, required=True, label='Nama kamu')
    email = forms.EmailField(max_length=200, required=True, label='Email')
    question = forms.CharField(max_length=2000, required=True, widget=forms.Textarea, label='Apa yang mau kamu tanyakan?')