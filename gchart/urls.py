from django.conf.urls import patterns, include, url
from gchart.views import GChartDemo

urlpatterns = patterns('',
                       url(r'^gcharts/', GChartDemo.as_view()),
                       )
