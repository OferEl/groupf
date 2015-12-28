from django.conf.urls import patterns, include, url
from django.contrib import admin
from groupf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyma_myweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url  (r'^admin/', include(admin.site.urls)),
    url  (r"^home/",include('home.urls' ),name='home' ),
    url  (r"^running/",include('running.urls' ),name='running' ),
    url  (r"^Walking/",include('Walking.urls' ),name='Walking' ),
    url  (r"^swimming/",include('swimming.urls' ),name='swimming' ),
    url  (r"^Bicycle/",include('Bicycle.urls' ),name='Bicycle' ),
    url  (r"^personal/",include('personal.urls' ),name='personal' ),
    url  (r"^tennis/",include('tennis.urls' ),name='tennis' ),
    url  (r"^account/", include('account.urls' ) ),


)


if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
        ,
    )