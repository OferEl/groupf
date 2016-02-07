from django import forms
from django.contrib.auth.models import User
from .models import Post




class post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_type', 'post_area', 'post_desc']
    
    def clean_post_desc(self):
        cd = self.cleaned_data
        if cd['post_desc'] != cd['post_desc']:
            raise forms.ValidationError('post_desc don\'t match.')
        return cd['post_desc']

