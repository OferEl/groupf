import logging
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, HttpResponseRedirect,HttpResponse,render
from django.views.generic import FormView
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


logger = logging.getLogger(__name__)
#@watch_login
def signin(request):
   
    # Force logout.
    if request.user.is_authenticated():
        login_failed = False
    else:
        logout(request)
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
    if request.POST:
        username = request.POST['username'].replace(' ', '').lower()
        password = request.POST['password']
        first_name = request.POST['first_name']
        email = request.POST['email']
        user = User.objects.create_user(username, password)

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
        user.first_name = 'Lennon'
        user.email = '123@gmail.com'
        l=user.save()
        return HttpResponseRedirect('/home/')
    else:
        return render(request,'signup.html')

    
