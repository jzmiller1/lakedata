from django.contrib.gis.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    investigator = models.CharField(max_length=20)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __unicode__(self):
        return self.project_name


class Site(models.Model):
    name = models.CharField(max_length=50)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    site_num = models.CharField(max_length=4)
    project_name = models.ForeignKey(Project)
    date = models.DateField()
    geom = models.PointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name


class WaterSample(models.Model):
    site = models.ForeignKey(Site) #forgien key to the primary key name in sample site class
    temp = models.FloatField(verbose_name='Temperature in Celsius')
    ph = models.FloatField(verbose_name='pH')
    do_mgl = models.FloatField(verbose_name='Dissolved Oxygen (mg/l)')
    sample_time = models.DateTimeField()
    depth = models.FloatField(verbose_name='Depth in Meters')
    turb = models.FloatField(verbose_name='Turbidity NTU')
    alky = models.FloatField(verbose_name='Alkalinity mg/l as CaCO_3')
    nh4 = models.FloatField(verbose_name='Ammonium (mg/l)')
    tot_n = models.FloatField(verbose_name='Total Nitrogen (mg/l)')
    tot_p = models.FloatField(verbose_name='Total Phosphorus (mg/l)')

    def __unicode__(self):
        return self.site.__unicode__() + " " + str(self.sample_time)

