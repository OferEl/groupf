from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name','user_type','gender','user_email','user_facebook','user_twitter']

admin.site.register(Profile, ProfileAdmin)