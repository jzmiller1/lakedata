from django.views import generic
from gchart.datasources import ModelDataSource
from gchart.models import DecimalData
from gchart.renderer import LineChart


class GChartDemo(generic.TemplateView):
    template_name = "gchart/demo.html"

    def get_context_data(self, **kwargs):
        context = super(GChartDemo, self).get_context_data(**kwargs)
        queryset = DecimalData.objects.filter(site=1)
        data_source = ModelDataSource(queryset, fields=["sample_time", "ph"])
        # print(data_source.data)
        # print(data_source.time_enabled)
        # print(data_source.get_header())
        # print(data_source.fields)
        # print(data_source.columns)
        chart = LineChart(data_source, options={
            'title': 'Demo Chart',
            'legend': {'alignment': "top", 'position': "right", 'textStyle': {'color': '#990033', 'fontSize': 20}},
            'fontSize': '30',
            'fontName': 'Pirate',
            'chartArea': {'width': 750, 'height': 250},
            'height': 400,
            'width': 1000,
            'backgroundColor': {'fill': 'transparent', 'stroke': '#B8B8B8', 'strokeWidth': 5},
            'axisTitlesPosition': 'out',
            'hAxis': {'title': 'Time', 'textStyle': {'fontSize': 20}, 'gridlines': {'color': '#FF9900'}, 'direction': 1},
            # 1 and -1 reverse the numbers on x axis, gridlines can control how many lines
            'vAxis': {'title': 'Demo Values', 'gridlines': {'color': '#990000'}, 'textStyle': {'fontName': 'BernhardMod BT', 'fontSize': 20}},
            })

        context.update({'chart': chart})
        return context
