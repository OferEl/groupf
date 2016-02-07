from django import forms
from django.contrib.auth.models import User
from account.models import Profile

class signin_form(forms.Form):
    Username = forms.CharField(label='Your name', max_length=50)
    Password = forms.CharField(label='Password', max_length=10)
    


class signup_form(forms.ModelForm):
    password = forms.CharField(label='Password', 
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', 
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class profileditform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name' ,'last_name' , 'user_type' ,'gender' , 'user_email' , 'user_facebook','user_twitter' ]


class usereditform(forms.ModelForm):
    class Meta:
        model = User
        fileds = ['username' , 'password']
