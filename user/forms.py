from dataclasses import field, fields
from django.forms import ModelForm
from .models import UserDetails, User

class UserDetailsForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['tanggal_lahir', 'bio_singkat']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields =  ['username', 'first_name', 'last_name', 'email']