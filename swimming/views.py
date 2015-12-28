from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf



def swimming_page (Request):

    return render(Request,"swimming.html",{'entries':'a'})