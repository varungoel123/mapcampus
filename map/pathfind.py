import heapq
from models import Node, Edge

class PathCostCalculator:
    def get_cost(self, start, end):
        return start.coordinates.distance(end.coordinates)

class HeuristicCostCalculator:
    def get_heuristic_cost(self, node, goal):
        return node.coordinates.distance(goal.coordinates)

class AStar:
    def __init__(self, path_calc, heuristic_calc):
        self.path_calc = path_calc
        self.heuristic_calc = heuristic_calc

    def find_path(self, start, goal):
        path_score = {start: 0}
        heuristic_score = {start: self.heuristic_calc.get_heuristic_cost(start, goal)}
        full_score = {start: path_score[start] + heuristic_score[start]}

        open_set = set()
        closed_set = set()
        parents = {}

        open_set.add(start)
        open_heap = [(full_score[start], start)]

        while open_set:
            entry = heapq.heappop(open_heap)            
            node = entry[1]

            if node == goal:
                return self.reconstruct_path(parents, start, goal)
            elif entry[0] != full_score[node]:
                continue
            
            open_set.remove(node)
            closed_set.add(node)
            
            for edge in Edge.objects.filter(node_src=node):
                adj = edge.node_sink
                if adj in closed_set:
                    continue

                pos_path_score = path_score[node] + self.path_calc.get_cost(node, adj)
                is_better = False

                if adj not in open_set:
                    open_set.add(adj)
                    heuristic_score[adj] = self.heuristic_calc.get_heuristic_cost(adj, goal)
                    is_better = True
                else:
                    is_better = pos_path_score < path_score[adj]

                if is_better:
                    parents[adj] = node
                    path_score[adj] = pos_path_score
                    full_score[adj] = pos_path_score + heuristic_score[adj]
                    heapq.heappush(open_heap, (full_score[adj], adj))
        return []

    def reconstruct_path(self, parents, start, goal):
        path = [goal]
        node = goal
        while node != start:
            node = parents[node]
            path.insert(0, node)
        return path

