#Implement a heap
import logging 
import random

logger = logging.getLogger(__name__)

class Heap(object):
    def update(self, cost, item):
        raise NotImplementedError
    def add(self, cost, item):
        raise NotImplementedError
    def delete(self, item):
        raise NotImplementedError
    def deleteMin(self):
        raise NotImplementedError
    def findmin(self):
        raise NotImplementedError
    def merge(self, h):
        raise NotImplementedError

class BinaryHeap(Heap):
    def __init__(self):
        self.data = []
        self.index = {}

    def _downheap(self, ci=0):
        li = 2*ci + 1 
        ckey, citem = self.data[ci]
        size = len(self.data)
        while(li < size): 
            lkey, litem = self.data[li]
            mi, mkey, mitem = li, lkey, litem
            if li + 1 < size:
                rkey, ritem = self.data[li + 1]
                if rkey < mkey:
                    mi, mkey, mitem = li + 1, rkey, ritem
            self.data[ci] = (mkey, mitem)
            self.index[mitem] = ci
            ci = mi
            li = 2*ci + 1
        self.index[citem] = ci
        self.data[ci] = (ckey, citem)
        self._upheap(ci)
    
    def _upheap(self, ci):
        if ci == 0:
            return
        ckey, citem = self.data[ci]
        while ci > 0:
            pi = (ci - 1)//2
            pkey, pitem = self.data[pi]
            if pkey <= ckey:
                break
            self.index[pitem] = ci
            self.data[ci] = pkey, pitem
            ci = pi
        self.index[citem] = ci
        self.data[ci] = ckey, citem

    def _update(self, key, item):
        index = self.index[item]
        (okey, oitem) = self.data[index]
        self.data[index] = (key, item)
        #logger.debug("ORIG:UPDATE: %s, %s" %(str(self.index), str(self.data)))
        if(okey < key):
            self._upheap(index)
        #logger.debug("UP:UPDATE: %s, %s" %(str(self.index), str(self.data)))
        if(okey > key):
            self._downheap(index)
        #logger.debug("DOWN:UPDATE: %s, %s" %(str(self.index), str(self.data)))

    def update(self, key, item):
        assert item in self.index
        self._update(key, item)

    def add(self, cost, item):
        #logger.debug("ORIG:ADD %s, %s, %d" %(str(self.index), str(self.data), len(self.data)))
        if item not in self.index:
            i = len(self.data)
            self.data.append((cost, item))
            self.index[item] = i 
            self._upheap(i)
        else:
            self._update(cost, item)
        #logger.debug("ADD %s, %s" %(str(self.index), str(self.data)))

    def findmin(self):
        if len(self.data) == 0:
            return None, None
        return self.data[0]

    def empty(self):
        return len(self.data) == 0

    def deleteMin(self):
        #logger.debug("ORIG:REMOVE %s, %s" %(str(self.index), str(self.data)))
        lcost, litem = self.data.pop()
        if(len(self.data) != 0):
            cost, item = self.data[0]
            self.data[0] = (lcost, litem)
            self.index[litem] = 0 
            self._downheap(0)
            #logger.debug("REMOVE %s, %s" %(str(self.index), str(self.data)))
        else:
            cost, item = lcost, litem
        assert item in self.index
        del self.index[item]
        return cost, item

    def check(self):
        return 
        size = len(self.data)
        for i in range(size):
            cost, item = self.data[i]
            assert item in self.index
            assert self.index[item] == i
            if i != 0:
                assert cost >= self.data[(i-1)//2][0]
            if 2*i + 1 < size:
                assert cost <= self.data[2*i + 1][0], "%d->%d:%s, %s" %(i, 2*i + 1, str(cost), str(self.data))
                if 2*i + 2 < size:
                    assert cost <= self.data[2*i + 2][0], "%d->%d:%s, %s" %(i, 2*i+2, str(cost), str(self.data[2*i + 2]))
        for key, value in self.index.items():
            assert key == self.data[value][1]

    def __repr__(self):
        return str(self.data)

from heapq import heappush, heappop
class BinaryHeapq(object):
    def __init__(self):
        self.heap = []
    def update(self, cost, item):
        raise NotImplementedError
    def add(self, cost, item):
        heappush(self.heap, (cost, item)) 
    def delete(self, item):
        raise NotImplementedError
    def deleteMin(self):
        return heappop(self.heap) 
    def findmin(self):
        raise NotImplementedError
    def merge(self, h):
        raise NotImplementedError
    def empty(self):
        return len(self.heap) == 0
    def check(self):
        pass

if __name__ == "__main__":
    h = BinaryHeap()
    N = 1000000
    logging.basicConfig(filename='heap.txt', level=logging.INFO)
    logger.disabled = True
    items = [random.randint(1, 1000) for i in range(N)]
    i = 0
    for item in items:
        h.add(item, i)
        h.check()
        i = i + 1
    prevkey = None
    print("Added %d items" %(N))
    i = 0
    while not h.empty():
        newkey = h.deleteMin()
        h.check()
        i = i + 1
        assert prevkey == None or prevkey <= newkey
    print("Removed %d items" %(i))
    
