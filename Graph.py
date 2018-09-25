# Basic graph class
# Currently implementing it as an adjacency list since that is generalizable
# Internally this is a dict of dicts
import numpy as np

class Graph(object):
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

    def _add_single_vertex(self, x, value):
        """
        Add a vertex, set its weight to 1
        If the vertex exists, return False since we did not add anything
        """
        if x in self.vertices:
            return False
        self.vertices[x] = value
        self.edges[x] = {}
        return True

    def add_vertex(self, x, value=1.0):
        """
        Add a vertex, set its weight to 1
        If the vertex exists, return False since we did not add anything
        """
        if isinstance(x, list):
            return [self._add_single_vertex(v, value) for v in x]
        return self._add_single_vertex(x, value) 

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
        self.edges[y][x] = value
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
        if x not in self.edges[y]:
            return False
        return True

    def remove_edge(self, x, y):
        if not self._test_edge(x, y):
            return False
        del self.edges[x][y]
        del self.edges[y][x]

    def get_vertex_value(self, x):
        if x not in self.vertices:
            return None
        return self.vertices[x] 

    def set_vertex_value(self, x, value):
        if x not in self.vertices:
            return False
        self.vertices[x] = value

    def get_edge_value(self, x, y):
        if not self._test_edge(x, y):
            return None 
        return self.edges[x][y]

    def set_edge_value(self, x, y, value):
        if not self._test_edge(x, y):
            return None 
        self.edges[x][y] = value
        self.edges[y][x] = value

    def adjacent(self, x, y):
        if x not in self.edges:
            return False
        if y not in self.edges:
            return False
        if y not in self.edges[x]:
            return False
        return True

    def neighbours(self, x):
        if x not in self.edges:
            return []
        return self.edges[x].keys()

    def adjMatrix(self):
        verts = self.vertices.keys()
        n = len(verts)
        mat = np.zeros((n, n))
        for row in range(n):
            vert = verts[row]
            edges = self.edges[vert]
            otherverts = edges.keys()
            for othervert in otherverts:
                col = verts.index(othervert)
                mat[row][col] = edges[othervert]
        return mat 

    def __repr__(self):
        val = ""
        for vert, value in self.vertices.items():
            val += "%s(%s):" %(str(vert), str(value))
            isFirst = True
            for overt, value in self.edges[vert].items():
                if not isFirst:
                    val += ","
                else:
                    isFirst = False
                val += "%s(%s)" %(str(overt), str(value))
            val += "\n"
        return val


if __name__ == "__main__":
    g = Graph()
    N = 10
    g.add_vertex(range(N))
    for i in range(1, N):
        g.add_edge(i-1, range(N))
    print g 
