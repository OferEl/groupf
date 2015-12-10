from django.conf.urls import patterns, include, url
from django.contrib import admin
from home.views import home_page
from groupf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyma_myweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url  (r'^admin/', include(admin.site.urls)),
    url(
       regex='',
       view=home_page,
       name='home_page', ),

url('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

)
