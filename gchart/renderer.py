import random
import string
import json
from django.template.loader import render_to_string

DEFAULT_HEIGHT = 400
DEFAULT_WIDTH = 800


def get_random_string():
    random_letter = lambda: random.choice(string.ascii_letters)
    random_string = "".join([random_letter()
                             for el in range(10)])
    return random_string


def get_default_options(graph_type="lines"):
    """ default options """
    options = {"series": {"{}".format(graph_type): {"show": "true"}},
               "legend": {"position": 'ne'},
               "title": "Chart"}
    return options


class BaseChart(object):
    def __init__(self, data_source, html_id=None,
                 width=None, height=None,
                 options=None, *args, **kwargs):
        self.data_source = data_source
        self.html_id = html_id or get_random_string()
        self.height = height or DEFAULT_HEIGHT
        self.width = width or DEFAULT_WIDTH
        self.options = options or {}
        self.columns = data_source.columns

    def get_data(self):
        return self.data_source.get_data()

    def get_data_json(self):
        json_data = json.dumps(self.get_data())
        json_data = json_data.replace('"new Date(', 'new Date(').replace(')```"',')')
        return json_data

    def get_options(self):
        options = self.options
        if not 'title' in options:
            options['title'] = "Chart"
        return options

    def get_options_json(self):
        return json.dumps(self.get_options())

    def get_template(self):
        raise NotImplementedError

    def get_html_id(self):
        return self.html_id

    def as_html(self):
        context = {"chart": self}
        return render_to_string(self.get_template(), context)


class LineChart(BaseChart):
    def get_template(self):
        return "gchart/line_chart.html"


class ColumnChart(BaseChart):
    def get_template(self):
        return "gchart/column_chart.html"


class BarChart(BaseChart):
    def get_template(self):
        return "gchart/bar_chart.html"

    def get_options(self):
        options = super(BarChart, self).get_options()
        if not 'vAxis' in options:
            vaxis = self.data_source.get_header()[0]
            options['vAxis'] = {'title': vaxis}
        return options

class CandlestickChart(BaseChart):
    def get_template(self):
        return "gchart/candlestick_chart.html"

class PieChart(BaseChart):
    def get_template(self):
        return "gchart/pie_chart.html"

class TreeMapChart(BaseChart):
    def get_template(self):
        return "gchart/treemap_chart.html"