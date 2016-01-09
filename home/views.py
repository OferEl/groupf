from django.shortcuts import render
def home_page (Request):
    return render(Request,"home.html",{'entries':'a'})
