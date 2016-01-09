from django import forms
from django.contrib.auth.models import User

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
        #model.last_name
        fields = ['username', 'email', 'password']
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']