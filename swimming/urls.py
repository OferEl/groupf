
from django.conf.urls import patterns, url
from swimming.views import swimming_page


urlpatterns = patterns('',
#    
    url(
        regex='',
        view=swimming_page,
        name='swimming',
    ),
   
)