from django.test import TestCase
from django.contrib.gis.geos import Point
#from mock import patch, Mock
from mapcampus.db.models import Node, Edge
from pathfind import AStar, PathCostCalculator, HeuristicCostCalculator

class TestAStar(TestCase):
    def setUp(self):
        new_york = Node(name="new york", coordinates=Point(40, 73))
        austin = Node(name="austin", coordinates=Point(30, 97))
        san_fran = Node(name="san fran", coordinates=Point(37, 122))
        chicago = Node(name="chicago", coordinates=Point(41, 87))

        new_york.save()
        austin.save()
        san_fran.save()
        chicago.save()

        Edge(node_a=new_york, node_b=austin).save()
        Edge(node_a=austin, node_b=new_york).save()

        Edge(node_a=austin, node_b=san_fran).save()
        Edge(node_a=san_fran, node_b=austin).save()

        Edge(node_a=san_fran, node_b=chicago).save()
        Edge(node_a=chicago, node_b=san_fran).save()

        Edge(node_a=chicago, node_b=new_york).save()
        Edge(node_a=new_york, node_b=chicago).save()

    def test_find_path(self):
        start = Node.objects.get(name="new york")
        goal = Node.objects.get(name="san fran")
        astar = AStar(PathCostCalculator(), HeuristicCostCalculator()) 
        
        for edge in astar.find_path(start, goal):
            print edge.node_a.name, '-->', edge.node_b.name
