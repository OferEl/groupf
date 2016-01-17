import logging
from django.shortcuts import render_to_response, HttpResponseRedirect,HttpResponse,render
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import signup_form
from django.contrib import messages
from account.forms import profile_form




logger = logging.getLogger(__name__)
#@watch_login
def signin(request):
   
    # Force logout.
    if request.user.is_authenticated():
        login_failed = False
    else:
        username = password = ''
        # Flag to keep track whether the login was invalid.
        login_failed = False

    if request.POST:
        username = request.POST['username'].replace(' ', '').lower()
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
        else:
            login_failed = True

    return render(request,'signin.html',
                              {'login_failed': login_failed},
                              context_instance=RequestContext(request))
    
def signup(request):
    if request.method == "POST":
        f=signup_form(request.POST)
        if  f.is_valid():
            password =request.POST['password']
            username =request.POST['username']
            email    =request.POST['email']
            user = User.objects.create_user(username,email,password)
            l=user.save()
            return render(request,'login_done.html',context_instance=RequestContext(request))
        else:
            return render(request,'signup.html',{'errors': f.errors})
    else:
        return render(request,'signup.html')

    
def profile(request):
    if request.method == "POST":
        profile_frm =profile_form(request.POST)
        if  profile_frm.is_valid():
            first_name =request.POST['first_name']
            last_name =request.POST['last_name']
            user_type =request.POST['user_type']
            user_email =request.POST['user_email']
            user_facebook =request.POST['user_type']
            user_twitter =request.POST['user_type']
            gender =request.POST['user_type']
            l=profile_frm.save()
            return render(request, "profile.html")
        else:
            return render(request, "profile.html")
    else:
        profile_frm =profile_form()
        return render(request, "profile.html" , {'user_profile' : profile_frm})


def logout_user(request):
    logout(request)
    return render(request, "home.html")