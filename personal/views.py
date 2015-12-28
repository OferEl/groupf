from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf



def personal_page (Request):

    return render(Request,"personal.html",{'entries':'a'})