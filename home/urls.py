
from django.conf.urls import patterns, url
from home.views import home_page


urlpatterns = patterns('',
#    
    url(
        regex='',
        view=home_page,
        name='home',
    ),

)