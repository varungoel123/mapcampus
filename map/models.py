from django.contrib.gis.db import models
from django.contrib import admin
from copy import deepcopy

class Node(models.Model):
    _NODE_TYPE_CHOICES = (('A', 'A'), ('B', 'B'))

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=_NODE_TYPE_CHOICES)
    coordinates = models.PointField(null=True)
    objects = models.GeoManager()

class Edge(models.Model):
    _EDGE_TYPE_CHOICES = (('A', 'A'), ('B', 'B'))

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=_EDGE_TYPE_CHOICES)
    node_src = models.ForeignKey(Node, related_name='edge_node_src')
    node_sink = models.ForeignKey(Node, related_name='edge_node_sink')
    objects = models.GeoManager()

    def undirected_save(self, *args, **kwargs):
        try:
            opp_edge = Edge.objects.get(node_src=self.node_sink, node_sink=self.node_src)
        except:
            opp_edge = deepcopy(self)
            opp_edge.id = None
            opp_edge.node_src, opp_edge.node_sink = opp_edge.node_sink, opp_edge.node_src

        opp_edge.save(args, kwargs)
        self.save(args, kwargs)


class NodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'type', 'coordinates']
    search_fields = ['name']

class EdgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'type', 'node_src', 'node_sink']
    search_fields = ['name']


#admin.site.register(Node, NodeAdmin)
#admin.site.register(Edge, EdgeAdmin)
