from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lakedata.views.home', name='home'),
    # url(r'^lakedata/', include('lakedata.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('frontpage.urls')),
    url(r'^lakedata/', include('lakedata.urls', namespace='data')),
    url(r'^contactabout/', include('contactabout.urls', namespace='contactabout')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
