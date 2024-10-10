from django.contrib.auth.forms import User,UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):
        first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
        last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
        email = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
        class Meta:
                model = User
                fields = ['username','first_name','last_name','email']

                def __str__(self):
                        return self.username