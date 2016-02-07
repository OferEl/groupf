from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf
from post.models import Post
from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = 'running.html'
    paginate_by = 10
    def get_queryset(self):
        return Post.objects.all()

