import logging
from Heap import BinaryHeap
import Random
import sys

def Djikstra(G, v1, v2=None):
    """
    Single Source shortest path
    Implement the Djikstras algorithm starting from node v1
    Return the edges
    """
    minNodes = BinaryHeap()
    minNodes.add(0, v1)
    for key in G.vertices.keys():
        G.vertices[key] = (None, None)
    G.vertices[v1] = (0, None)
    while not minNodes.empty():
        (dist, v) = minNodes.deleteMin()
        assert G.vertices[v] != None
        for otherv in G.neighbours(v):
            weight = G.get_edge_value(v, otherv)
            ndist = dist + weight
            cdist, cprev = G.vertices[otherv]
            if cdist == None or ndist < cdist:
                G.vertices[otherv] = (ndist, v)
                minNodes.add(ndist, otherv)
    return G.vertices

def BellmannFord(G, v1, v2=None):
    """
    Single Source shortest path generic case where weights can be negative
    This is a O(VE) algorithm
    """
    for key in G.vertices.keys():
        G.vertices[key] = (sys.float_info.max, None)
    G.vertices[v1] = (0, None)
    for i in range(len(G.vertices.keys())):
        for vkey, edges in G.edges.items():
            vw = G.vertices[vkey][0]
            if(vw < sys.float_info.max):
                for ovkey, weight in edges.items():
                    ovw = G.vertices[ovkey][0] 
                    if vw + weight < ovw:
                        G.vertices[ovkey] = (vw + weight, vkey)

    for vkey, edges in G.edges.items():
        for ovkey, weight in edges.items():
            if G.vertices[vkey][0] + weight < G.vertices[ovkey][0]:
                assert "Graph with a negative-weight cycle"

    return G.vertices

if __name__=="__main__":
    #G = Random.path_graph(10)
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='ssp.txt', level=logging.INFO)
    logger.setLevel(logging.DEBUG)
    G = Random.random_skew_graph(50, 0.2)
    dj = Djikstra(G, 0)
    print("DJIKSTRA:")
    print(dj)
    bf = BellmannFord(G, 0)
    print("BELLMANN-FORD:")
    print(bf)
    assert bf == dj

