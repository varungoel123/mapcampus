from abc import ABCMeta, abstractmethod  
from mapcampus.db.models import Point 
  
class PathFinder:  
    __metaclass__ = ABCMeta  
 
    @abstractmethod  
    def find_path(start, goal):
        pass

    @abstractmethod
    def find_path(*args, **kwargs):
        pass

class AStar(PathFinder):
    def find_path(start, goal):
        return 1

    def find_path(*args, **kwargs):
        return 1
