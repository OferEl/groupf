
from django.conf.urls import patterns, url
from .views import post_page

#urlpatterns = patterns('',
#    url(r'^post/$',post_page.as_view(),
#        name='post',),
#)

urlpatterns = patterns('',

    url(
        regex='',
       view=post_page,
        name='post',
    ),
   
)