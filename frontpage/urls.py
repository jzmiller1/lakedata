from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import MainView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', MainView.as_view(), name='main_page'),
)
