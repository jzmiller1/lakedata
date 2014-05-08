from decimal import Decimal
import datetime


class BaseDataSource(object):
    def __init__(self, *args, **kwargs):
        pass

    def get_data(self):
        """Get all the data."""
        raise NotImplementedError


class SimpleDataSource(BaseDataSource):
    def __init__(self, data):
        self.data = data
        self.columns = []

    def get_data(self):
        return self.data


class ModelDataSource(SimpleDataSource):
    def __init__(self, queryset, fields=None):
        self.queryset = queryset
        if fields:
            self.fields = fields
        else:
            self.fields = [el.name for el in self.queryset.model._meta.fields]
        #print(self.fields) ['sample_time', 'ph']
        self.data = self.create_data()
        self.columns = self.create_columns()

    def create_columns(self):
        columns = []
        values = self.data[1]
        type_map = {str: 'string',
                    datetime.datetime: 'datetime',
                    float: 'number',
                    unicode: 'string',
                    int: 'number',
                    bool: 'boolean'}

        for (field, data) in zip(self.fields, values):
            if isinstance(data, datetime.datetime):
                columns.append((field,
                                'datetime'))
            elif isinstance(data, str) and "new Date" in data:
                columns.append((field,
                                'datetime'))
            else:
                columns.append((field,
                                type_map[type(data)]))
        return columns

    def create_data(self):
        data = []
        for row in self.queryset:
            data.append(self.get_field_values(row, self.fields))
        return data

    def get_field_values(self, row, fields):
        data = []
        for field in fields:
            d = getattr(row, field)
            if isinstance(d, Decimal):
                data.append(float(d))
            elif isinstance(d, datetime.datetime):
                d = d.timetuple()
                t = "{},{},{},{},{},{}".format(d.tm_year,
                                               d.tm_mon - 1,
                                               d.tm_mday,
                                               d.tm_hour,
                                               d.tm_min,
                                               d.tm_sec
                )

                data.append("new Date({})```".format(t))
            else:
                data.append(d)
        return data


