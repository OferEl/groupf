from django.shortcuts import render
from .forms import post
from django.contrib import messages
from django.views.generic.edit import CreateView
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required
def post_page(request):
    if request.method == 'POST':
       post_form = post(request.POST  )
       if post_form.is_valid():
           pf=post_form.save(commit=False)
           pf.user=request.user
           pf.save()
           messages.success(request, 'post added successfully')
           return render(request, "post.html")
       else:
           return render(request, "post.html",{'post_form': post_form})
    else:
        post_form = post()
        return render(request, "post.html",{'post_form': post_form})

