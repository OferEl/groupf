from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf


def home_page (Request):
    return render(Request,"home.html",{'entries':'a'})