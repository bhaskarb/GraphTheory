#Random graph
from DiGraph import DiGraph
from Graph import Graph
import math 
import random

def isolated_graph(n, directed=False):
    """
    Isolated Graph with no edges and n vertices
    """
    if directed:
        G = DiGraph()
    else:
        G = Graph()
    G.add_vertex(range(n))
    return G

def complete_graph(n, directed=False):
    """
    Fully connected graph with n(n-1)/2 edges and n vertices
    """
    if directed:
        G = DiGraph()
    else:
        G = Graph()
    G.add_vertex(range(n))
    for i in range(n):
        G.add_edge(i, range(i + 1, n))
    return G

def path_graph(n, cyclic=True, directed=True):
    """
    Line graph with n nodes and n-1 edges
    """
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
            if random.random() < p and ((not directed and i < j) or (directed and i != j)):
                G.add_edge(i, j)
    return G

def random_skew_graph(n, p, diesize=10):
    """
    Erdos Renyi Graph of n vertices
    Probabilty of an edge is p
    """
    G = path_graph(n, True, True)
    vs = G.vertices.keys()
    num = len(vs)
    for v in vs:
        G.vertices[v] = (random.randint(1, diesize), random.randint(1, diesize))
        G.vertices[v] = (diesize*0.5*math.cos(math.pi*2*v/num), diesize*0.5*math.sin(math.pi*2*int(v)/num))   
    for i in range(n):
        loci = G.vertices[i]
        for j in range(n):
            locj = G.vertices[j]
            distance = math.sqrt((loci[0]- locj[0])**2 + (loci[1] - locj[1])**2)
            value = max(random.random()*distance, 0.1)
            if j == i + 1:
                G.set_edge_value(i, j, value)
            elif random.random() < p:
                G.add_edge(i, j, value)
    return G

import matplotlib.pyplot as plt
#import matplotlib.patches import Circle
def plot(G):
    plt.xticks([])
    plt.yticks([])
    delta = 0.2
    xmin = ymin = 100
    xmax = ymax = 0
    for v, pos in G.vertices.items():
        plt.text(float(pos[0]), float(pos[1]), str(v), color='blue', ha='center', va='center', fontsize=14)
#        plt.circle( float(pos[0]), float(pos[1]) , delta)
        xmin = min(xmin, pos[0])
        ymin = min(ymin, pos[1])
        xmax = max(xmax, pos[0])
        ymax = max(ymax, pos[1])
    for fvert, edict in G.edges.items():
        xf, yf = G.vertices[fvert]
        for tvert, weight in edict.items():
            xt, yt = G.vertices[tvert]
            thetha = math.atan2(yt - yf, xt - xf)
            dx = delta*math.cos(thetha)
            dy = delta*math.sin(thetha)
            #print xt, xf, dx, yt, yf, dy
            plt.arrow(xf + dx, yf + dy, (xt - xf) - 2*dx, (yt - yf) - 2*dy, length_includes_head=True, shape='full', head_starts_at_zero=True, head_width=0.1)
            plt.text((xt + xf)/2.0, (yt + yf)/2.0, str("%0.2f" %(weight)), color='red')
    plt.xlim(xmin-0.5, xmax+0.5)
    plt.ylim(ymin-0.5, ymax+0.5)



if __name__ == "__main__":
#    print complete_graph(10)
#    print isolated_graph(10)
#    print erdos_renyi(10, 0.5, True)
    G = random_skew_graph(10, 0.1)
    plot(G)
    plt.show()

