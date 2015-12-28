from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf



def Bicycle_page (Request):

    return render(Request,"Bicycle.html",{'entries':'a'})