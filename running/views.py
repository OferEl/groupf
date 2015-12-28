from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf



def running_page (Request):

    return render(Request,"running.html",{'entries':'a'})