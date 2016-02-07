import logging
from django.shortcuts import render_to_response, HttpResponseRedirect,HttpResponse,render
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import signup_form
from account.forms import profileditform ,usereditform
from django.contrib.auth.decorators import login_required
from .models import Profile




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
            new_user = User.objects.create_user(username,email,password)
            l=new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request,'login_done.html',context_instance=RequestContext(request))
        else:
            return render(request,'signup.html',{'errors': f.errors})
    else:
        return render(request,'signup.html')

@login_required
def profile(request):
    if request.method == "POST":
        user_frm = usereditform(instance=request.user,data=request.POST)
        profile_frm =profileditform(instance=request.user.profile,data=request.POST)
        if  profile_frm.is_valid() and user_frm.is_valid():
            l=profile_frm.save()
            m=user_frm.save()
        else:
            return render(request, "profile.html",{'user_form': user_frm,'profile_form': profile_frm} )
    else:
        user_frm = usereditform(instance=request.user)
        profile_frm =profileditform(instance=request.user.profile)

    return render(request,"profile.html",{'user_form': user_frm,'profile_form': profile_frm})



def logout_user(request):
    logout(request)
    return render(request, "home.html")