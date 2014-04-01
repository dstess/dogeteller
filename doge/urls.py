from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^blog/', include('blog.foo.urls')),
    (r'^$','doge.views.index'),
    url(r'^submit/$', 'doge.views.submit'),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
    #url(r'^submit/?Year=(?P<year>\d{4})/$', 'doge.views.submit'), 
    #url(r'^submit/(?P<year>/d{4})/$', 'doge.views.submit', name="submit"), 
    

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    #(r'^submit.html/', include(submit.site.urls)),
)
