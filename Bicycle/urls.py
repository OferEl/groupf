
from django.conf.urls import patterns, url
from Bicycle.views import Bicycle_page

urlpatterns = patterns('',
#    
    url(
        regex='',
        view=Bicycle_page,
        name='Bicycle',
    ),
   
)