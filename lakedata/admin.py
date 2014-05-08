from django.contrib.gis import admin
from lakedata.models import Project, Site, WaterSample

admin.site.register(Project)
admin.site.register(Site, admin.GeoModelAdmin)
admin.site.register(WaterSample)


