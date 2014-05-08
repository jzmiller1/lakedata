from django.views import generic
from gchart.datasources import ModelDataSource
from gchart.renderer import LineChart
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.db.models import Avg, Max, Min, Variance, StdDev, Count
from lakedata.models import WaterSample, Site
from lakedata.forms import SiteSelectionForm, MultiYearSelectionForm
from django.core.urlresolvers import reverse


class SiteMapView(TemplateView):
     template_name = 'lakedata/sitemap.html'


class SelectSample(generic.FormView):
    template_name = 'lakedata/siteselect.html'
    form_class = SiteSelectionForm

    def form_valid(self, form, **kwargs):
        return redirect(reverse('data:multiyear', kwargs={'site': form.cleaned_data['site'].site_num,
                                                      'syear': form.cleaned_data['year'][0],
                                                      'eyear': form.cleaned_data['year'][0],
                                                      }))


class SelectMultiYear(generic.FormView):
    template_name = 'lakedata/selectmultiyear.html'
    form_class = MultiYearSelectionForm

    def form_valid(self, form, **kwargs):
        return redirect(reverse('data:multiyear', kwargs={'site': form.cleaned_data['site'].site_num,
                                                      'syear': form.cleaned_data['syear'][0],
                                                      'eyear': form.cleaned_data['eyear'][0],
                                                      }))


class SampleVsAverageFormPage(generic.TemplateView):
    template_name = 'lakedata/watersample_vsaverage.html'

    def get_context_data(self, **kwargs):
        fields = [row for row in WaterSample._meta.fields if not isinstance(row.verbose_name, unicode)]
        context = super(SampleVsAverageFormPage, self).get_context_data(**kwargs)
        charts = []
        queryset = WaterSample.objects.filter(site=context['site'],
                                                  sample_time__gte='{}-01-01'.format(context['syear']),
                                                  sample_time__lte='{}-12-31'.format(context['eyear'])).order_by('sample_time')
        for field in fields:


            data_source = ModelDataSource(queryset, fields=["sample_time", field.name])

            chart = LineChart(data_source, options={

                'title': field.verbose_name,
                'legend': {'alignment': "top", 'position': "right", 'textStyle': {'color': '#990033', 'fontSize': 20}},
                'fontSize': '30',
                'fontName': 'Pirate',
                'chartArea': {'width': 750, 'height': 250},
                'height': 400,
                'width': 1000,
                'backgroundColor': {'fill': 'transparent', 'stroke': '#B8B8B8', 'strokeWidth': 5},
                'axisTitlesPosition': 'out',
                'hAxis': {'title': 'Date', 'textStyle': {'fontSize': 20}, 'gridlines': {'color': '#FF9900'}, 'direction': 1},
                # 1 and -1 reverse the numbers on x axis, gridlines can control how many lines
                'vAxis': {'title': field.verbose_name, 'gridlines': {'color': '#990000'}, 'textStyle': {'fontName': 'BernhardMod BT', 'fontSize': 20}},
                })

            chart.avg = WaterSample.objects.filter(sample_time__gte='{}-01-01'.format(context['syear']),
                                                   sample_time__lte='{}-12-31'.format(context['eyear']),
                                                   site=context['site']).aggregate(Avg(field.name))['{}__avg'.format(field.name)]

            chart.min = WaterSample.objects.filter(sample_time__gte='{}-01-01'.format(context['syear']),
                                                   sample_time__lte='{}-12-31'.format(context['eyear']),
                                                   site = context['site']).aggregate(Min(field.name))['{}__min'.format(field.name)]

            chart.max = WaterSample.objects.filter(sample_time__gte='{}-01-01'.format(context['syear']),
                                                   sample_time__lte='{}-12-31'.format(context['eyear']),
                                                   site = context['site']).aggregate(Max(field.name))['{}__max'.format(field.name)]

            chart.cnt = WaterSample.objects.filter(sample_time__gte='{}-01-01'.format(context['syear']),
                                                   sample_time__lte='{}-12-31'.format(context['eyear']),
                                                   site = context['site']).aggregate(Count(field.name))['{}__count'.format(field.name)]

            chart.std_dev = WaterSample.objects.filter(sample_time__gte='{}-01-01'.format(context['syear']),
                                                       sample_time__lte='{}-12-31'.format(context['eyear']),
                                                       site = context['site']).aggregate(StdDev(field.name))['{}__stddev'.format(field.name)]

            chart.var = WaterSample.objects.filter(sample_time__gte='{}-01-01'.format(context['syear']),
                                                   sample_time__lte='{}-12-31'.format(context['eyear']),
                                                   site = context['site']).aggregate(Variance(field.name, sample=False))['{}__variance'.format(field.name)]
            charts.append(chart)

        name = Site.objects.filter(site_num=context['site'])[0].name

        context.update({'name': name, 'charts': charts})
        return context