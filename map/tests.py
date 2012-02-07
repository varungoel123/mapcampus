from django.test import TestCase
from django.contrib.gis.geos import Point
from models import Node, Edge
from pathfind import AStar, PathCostCalculator, HeuristicCostCalculator

class TestAStar(TestCase):
    def setUp(self):
        new_york = Node(name='new york', coordinates=Point(40, 73))
        austin = Node(name='austin', coordinates=Point(30, 97))
        san_fran = Node(name='san fran', coordinates=Point(37, 122))
        chicago = Node(name='chicago', coordinates=Point(41, 87))

        new_york.save()
        austin.save()
        san_fran.save()
        chicago.save()

        Edge(node_src=new_york, node_sink=chicago).save()
        Edge(node_src=chicago, node_sink=san_fran).save()

        Edge(node_src=new_york, node_sink=austin).save()
        Edge(node_src=austin, node_sink=san_fran).save()

        Edge(node_src=san_fran, node_sink=new_york).save()
        
    def test_find_path(self):
        start = Node.objects.get(name='new york')
        goal = Node.objects.get(name='san fran')
        astar = AStar(PathCostCalculator(), HeuristicCostCalculator()) 
                
        path = astar.find_path(start, goal)
        self.assertEqual(path[0].name, 'new york')
        self.assertEqual(path[1].name, 'chicago')
        self.assertEqual(path[2].name, 'san fran')

