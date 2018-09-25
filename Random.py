#Random graph
from DiGraph import DiGraph
from Graph import Graph
import math 
import random

def isolated_graph(n, directed=False):
    if directed:
        G = DiGraph()
    else:
        G = Graph()
    G.add_vertex(range(n))
    return G

def complete_graph(n, directed=False):
    if directed:
        G = DiGraph()
    else:
        G = Graph()
    G.add_vertex(range(n))
    for i in range(n):
        G.add_edge(i, range(i + 1, n))
    return G

def path_graph(n, cyclic=True, directed=True):
    if directed:
        G = DiGraph()
    else:
        G = Graph()
    G.add_vertex(range(n))
    for i in range(n-1):
        G.add_edge(i, i + 1)
    if cyclic:
        G.add_edge(n-1, 0)
    return G

def erdos_renyi(n, p, directed=False):
    """
    Erdos Renyi Graph of n vertices
    Probabilty of an edge is p
    """
    if p >= 1:
        return complete_graph(n, directed)
    if not directed:
        G = Graph()
    else:
        G = DiGraph()
    G.add_vertex(range(n))
    if p <= 0:
        return G  
    for i in range(n):
        for j in range(n):
            if random.random() < p and ((directed and i > j) or (not directed and i != j)):
                G.add_edge(i, j)
    return G

def random_skew_graph(n, p, diesize=10):
    """
    Erdos Renyi Graph of n vertices
    Probabilty of an edge is p
    """
    G = path_graph(n, True, True)
    vs = G.vertices.keys()
    locations = {}
    for v in vs:
        locations[v] = (random.randint(1, diesize), random.randint(1, diesize))
    for i in range(n):
        loci = locations[i]
        for j in range(n):
            locj = locations[j]
            distance = math.sqrt((loci[0]- locj[0])**2 + (loci[1] - locj[1])**2)
            value = max(random.random()*distance, 1)
            if j == i + 1:
                print i, j, value
                G.set_edge_value(i, j, value)
            elif random.random() < p:
                print i, j, value
                G.add_edge(i, j, value)
    return G

if __name__ == "__main__":
#    print complete_graph(10)
#    print isolated_graph(10)
#    print erdos_renyi(10, 0.5, True)
    print random_skew_graph(40, 0.1)
