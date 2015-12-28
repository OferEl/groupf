
from django.conf.urls import patterns, url
from running.views import running_page

urlpatterns = patterns('',
#    
    url(
        regex='',
        view=running_page,
        name='running',
    ),
   
)