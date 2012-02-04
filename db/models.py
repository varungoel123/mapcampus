from django.db import models
from django.contrib import admin

# Credit goes to user185534 at stackoverflow.com
class EnumField(models.Field):
    def __init__(self, values):
        self.values = values
        super(EnumField, self).__init__(
            choices=[(v, v) for v in self.values],
            default=self.values[0]
        )

    def db_type(self):
        return 'enum({0})'.format( ','.join("'%s'" % v for v in self.values))

class Point(models.Model):
    _POINT_STATUSES = ['a', 'b']
    _POINT_TYPES = ['a', 'b']

    name = models.CharField(max_length=50)
    status = EnumField(_POINT_STATUSES)
    type = EnumField(_POINT_TYPES)
    lat = models.IntegerField(default=0)
    lng = models.IntegerField(default=0)

class PointAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'type', 'lat', 'lng']
    search_fields = ['name']

class Line(models.Model):
    _LINE_STATUSES = ['a', 'b']
    _LINE_TYPES = ['a', 'b']

    name = models.CharField(max_length=50)
    status = EnumField(_LINE_STATUSES)
    type = EnumField(_LINE_TYPES)
    point_a = models.ForeignKey(Point)
    point_b = models.ForeignKey(Point)

class LineAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'type', 'point_a', 'point_b']
    search_fields = ['name']


admin.site.register(Point, PointAdmin)
admin.site.register(Line, LineAdmin)

