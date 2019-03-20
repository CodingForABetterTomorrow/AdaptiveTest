from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user=super(SignUpForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user

class RawQuestion(forms.Form):
    ques = forms.CharField(widget=forms.TextInput())
    optionA = forms.CharField(widget=forms.TextInput())
    optionB = forms.CharField(widget=forms.TextInput())
    optionC = forms.CharField(widget=forms.TextInput())
    optionD = forms.CharField(widget=forms.TextInput())
    rightAns = forms.CharField(widget=forms.TextInput())
    diff = forms.CharField(widget=forms.TextInput())
    field =  forms.CharField(widget=forms.TextInput())
    origin = forms.CharField(widget=forms.TextInput())

class RawTest(forms.Form):
    TestID =forms.CharField(widget=forms.TextInput())
    passwd = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.TextInput())
    Company = forms.CharField(widget=forms.TextInput())
    math = forms.IntegerField(widget=forms.TextInput())
    lr = forms.IntegerField(widget=forms.TextInput())
    eng = forms.IntegerField(widget=forms.TextInput())


