
from django.conf.urls import patterns, url
from running.views import PostListView


urlpatterns = patterns('',
    url(r'^post/$',PostListView.as_view(),name='running',),
)