
from django.conf.urls import patterns, url
from Walking.views import Walking_page

urlpatterns = patterns('',
#    
    url(
        regex='',
        view=Walking_page,
        name='Walking',
    ),
   
)