from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf


def Walking_page (Request):

    return render(Request,"Walking.html",{'entries':'a'})