
from django.conf.urls import patterns, url
from tennis.views import tennis_page

urlpatterns = patterns('',
#    
    url(
        regex='',
        view=tennis_page,
        name='tennis',
    ),
   
)