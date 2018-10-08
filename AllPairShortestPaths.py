import numpy as np
from Heap import BinaryHeap
import Random
import sys
import logging 

logger = logging.getLogger(__name__)

def FloydWarshall(G):
    """
    All Pair shortest path
    O(n^3) will deal with negative edges
    """
    dist = G.adjMatrix(np.inf)
    v, col = dist.shape
    assert v == col
    closest = np.full((v,v), np.inf) 
    for xRow in range(v):
        for yRow in range(v):
            if dist[xRow][yRow] != np.inf:
                closest[xRow][yRow] = xRow
    for xRow in range(v):
        dist[xRow][xRow] = 0
    logger.debug(dist)
    logger.debug(closest)

    for k in range(v):
        logger.debug("K=" + str(k))
        for i in range(v):
           for j in range(v):
                logger.debug(i, j, k, dist[i][j], dist[i][k], dist[k][j])
                if dist[i][j] > dist[i][k] + dist[k][j]:
                   dist[i][j] = dist[i][k] + dist[k][j]
                   closest[i][j] = closest[k][j]
        logger.debug(dist)
        logger.debug(closest)
    return dist, closest

if __name__=="__main__":
    G = Random.random_skew_graph(10, 0.2)
    np.set_printoptions(precision=2)
    print FloydWarshal(G)

