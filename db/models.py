from django.contrib.gis.db import models
from django.contrib import admin

class Node(models.Model):
    _NODE_STATUS_CHOICES = (('A', 'A'), ('B', 'B'))
    _NODE_TYPE_CHOICES = (('A', 'A'), ('B', 'B'))

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=_NODE_STATUS_CHOICES)
    type = models.CharField(max_length=1, choices=_NODE_TYPE_CHOICES)
    coordinates = models.PointField(null=True)
    objects = models.GeoManager()

class Edge(models.Model):
    _EDGE_STATUS_CHOICES = (('A', 'A'), ('B', 'B'))
    _EDGE_TYPE_CHOICES = (('A', 'A'), ('B', 'B'))

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=_EDGE_STATUS_CHOICES)
    type = models.CharField(max_length=1, choices=_EDGE_TYPE_CHOICES)
    node_a = models.ForeignKey(Node, related_name='edge_node_a')
    node_b = models.ForeignKey(Node, related_name='edge_node_b')
    objects = models.GeoManager()

class NodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'type', 'coordinates']
    search_fields = ['name']

class EdgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'type', 'node_a', 'node_b']
    search_fields = ['name']


#admin.site.register(Node, NodeAdmin)
#admin.site.register(Edge, EdgeAdmin)
