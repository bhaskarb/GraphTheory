# Basic graph class
# Currently implementing it as an adjacency list since that is generalizable
# Internally this is a dict of dicts
import numpy as np
from Graph import Graph 

class DiGraph(Graph):
    """
    This class is a basic graph object which describes a undirected graph
    The basic operations corespond to a graph ADT namely:
    adjacent(G, x, y): check if there is an edge between x and y
    neigbours(G, x): return list of all neighbours vertices to x
    add_vertex(G, x): Add a vertex x to G
    remove_vertex(G, x): remove the vertex x if it exists in G
    add_edge(G, x, y, v?): add an edge between x, y with value if not there
    remove_edge(G, x, y): remove edge x, y in G
    get_vertex_value(G, x): Get the value of the vertex x in G
    set_vertex_value(G, x, value): Get the value of vertex x in G
    get_edge_value(G, x, y): Return the edge value
    set_edge_value(G, x, y, v): Set the edge value

    For this iteration lets assume that the edge and vertex values are numbers
    """
    def __init__(self):
        self.vertices = {} #Dict of value
        self.edges = {} #Dict of dict, self.edges[vertex] = dict whose key is a vertex and value is the edge weight

    def _remove_single_vertex(self, x):
        """
        Add a vertex, set its weight to 1
        return False if the vertex does not exist
        """
        if x not in self.vertices:
            return False
        del self.vertices[x]
        for vert in self.edges[x].keys():
            del self.edges[vert][x]
        del self.edges[x]

    def remove_vertex(self, x):
        """
        Add a vertex, set its weight to 1
        return False if the vertex does not exist
        """
        if isinstance(x, list):
            return [self._add_single_vertex(v) for v in x]
        return self._remove_single_vertex(x)

    def _add_single_edge(self, x, y, value):
        if x not in self.edges:
            return False
        if y not in self.edges:
            return False
        self.edges[x][y] = value
        return True

    def add_edge(self, x, y, value=1.0):
        if isinstance(x, list) and isinstance(y, list):
            raise NotImplementedError
        if isinstance(x, list):
            return [ self._add_single_edge(v, y, value) for v in x ]
        if isinstance(y, list):
            return [ self._add_single_edge(x, v, value) for v in y ]
        return self._add_single_edge(x,y, value)

    def _test_edge(self, x, y):
        if x not in self.edges:
            return False
        if y not in self.edges:
            return False
        if y not in self.edges[x]:
            return False
        return True

    def remove_edge(self, x, y):
        if not self._test_edge(x, y):
            return False
        del self.edges[x][y]

    def get_edge_value(self, x, y):
        if not self._test_edge(x, y):
            return None 
        return self.edges[x][y]

    def set_edge_value(self, x, y, value):
        assert self._test_edge(x, y)
        self.edges[x][y] = value

if __name__ == "__main__":
    g = DiGraph()
    N = 10
    g.add_vertex(range(N))
    for i in range(N):
        g.add_edge(i, range(i+1, N))
    print g.adjMatrix()
