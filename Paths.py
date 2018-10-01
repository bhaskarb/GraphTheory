from Heap import Heap
import Random

def Djikstra(G, v1, v2=None):
    """
    Single Source shortest path
    Implement the Djikstras algorithm starting from node v1
    Return the edges
    """
    minNodes = Heap()
    minNodes.add(0, v1)
    for key in G.vertices.keys():
        G.vertices[key] = (None, None)
    G.vertices[v1] = (0, None)
    while not minNodes.empty():
        (dist, v) = minNodes.remove()
        assert G.vertices[v] != None
        for otherv in G.neighbours(v):
            weight = G.get_edge_value(v, otherv)
            ndist = dist + weight
            cdist, cprev = G.vertices[otherv]
            if cdist == None or ndist < cdist:
                G.vertices[otherv] = (ndist, v)
                minNodes.add(ndist, otherv)
    return G.vertices


if __name__=="__main__":
    G = Random.path_graph(10)
    print Djikstra(G, 0)

