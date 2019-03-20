from django import forms
from .models import Student

class CandidateRegisterForm(forms.Form):
	testid = forms.CharField(label='Test Id')
	testpassword = forms.CharField(label='Test Password',widget=forms.PasswordInput)
	studentname = forms.CharField(label='Your Full Name')
	studentemail = forms.EmailField(label='Your Email id')