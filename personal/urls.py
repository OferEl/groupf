
from django.conf.urls import patterns, url
from personal.views import personal_page

urlpatterns = patterns('',
#    
    url(
        regex='',
        view=personal_page,
        name='personal',
    ),
   
)