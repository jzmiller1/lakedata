from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from lakedata.views import SelectSample,SampleVsAverageFormPage, SiteMapView, SelectMultiYear
from djgeojson.views import GeoJSONLayerView
from lakedata.models import Site

urlpatterns = patterns(
    '',
    url(r'^selectsample/$', login_required(SelectSample.as_view()), name='selectsample'),
    url(r'^selectmultiyear/$', login_required(SelectMultiYear.as_view()), name='selectmultiyear'),
    url(r'^multiyear/(?P<site>\d+)/(?P<syear>\d+)/(?P<eyear>\d+)/$', login_required(SampleVsAverageFormPage.as_view()), name='multiyear'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Site, geometry_field='geom', simplify=True, properties=('name',)), name='sites'),
    url(r'^sitemap/$', SiteMapView.as_view(), name="sitemap"),
)