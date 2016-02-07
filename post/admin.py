from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['post_id', 'user', 'post_type','post_area','post_date']

admin.site.register(Post, PostAdmin)