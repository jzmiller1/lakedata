from django.contrib import admin
from django.conf.urls import patterns, include,  url
from contactabout.views import AboutDetail,  ContactFormView, ContactConfirmation

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^contact', ContactFormView.as_view(), name='contact'),
    url(r'^confirmation/', ContactConfirmation.as_view(), name='confirmation'),
    url(r'^(?P<pk>\d+)/$', AboutDetail.as_view(), name='detail_about_page'),
)
