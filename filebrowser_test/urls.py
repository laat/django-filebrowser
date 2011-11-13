from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from filebrowser.sites import site as filebrowser
from filebrowser.versions.sites import site as versionfilebrowser

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'filebrowser_test.views.home', name='home'),
    # url(r'^filebrowser_test/', include('filebrowser_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^filebrowser/', include(filebrowser.urls)),
    url(r'^versionfilebrowser/', include(versionfilebrowser.urls)),
)