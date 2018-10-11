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
        self.size = 0

    def _parent(self, i):
        if i == 0 or self.empty():
            return -1
        return (i-1)//2

    def _child(self, i, left=True):
        if self.empty():
            return -1
        if left:
            j = i*2 + 1
        else:
            j = i*2 + 2
        if j < self.size:
            return j
        return -1
    
    def empty(self):
        return self.size == 0

    def _downheap(self, ci=0):
        li = self._child(ci, True)
        ri = self._child(ci, False)
        ckey, citem = self.data[ci]
        mi = ci
        #logger.debug(ci, ckey, citem)
        if li >=0 and ri >=0:
            lkey, litem = self.data[li]
            rkey, ritem = self.data[ri]
            #logger.debug( li, lkey, litem)
            #logger.debug( ri, rkey, ritem)
            if lkey < ckey and lkey <= rkey:
                mi, mkey, mitem = li, lkey, litem
            elif rkey < ckey and rkey  < lkey:
                mi, mkey, mitem = ri, rkey, ritem
        elif li >=0:
            lkey, litem = self.data[li]
            #logger.debug( li, lkey, litem)
            if lkey < ckey:
                mi, mkey, mitem = li, lkey, litem
        elif ri >=0:
            rkey, ritem = self.data[ri]
            #logger.debug( ri, rkey, ritem)
            if rkey < ckey:
                mi, mkey, mitem = ri, rkey, ritem
        if mi != ci:
            self.data[ci] = (mkey, mitem)
            self.data[mi] = (ckey, citem)
            self.index[mitem] = ci
            self.index[citem] = mi
            self._downheap(mi)
   
    def _upheap(self, ci):
        pi = self._parent(ci)
        if pi >= 0:
            pkey, pitem = self.data[pi]
            ckey, citem = self.data[ci]
        #    #logger.debug ci, pi,ckey, pkey
            if ckey < pkey:
                self.data[pi] = ckey, citem
                self.data[ci] = pkey, pitem
                assert ci != pi
                self.index[pitem] = ci
                self.index[citem] = pi
                self._upheap(pi)

    def _update(self, key, item):
        index = self.index[item]
        self.data[index] = (key, item)
        #logger.debug("ORIG:UPDATE: %s, %s" %(str(self.index), str(self.data[0:self.size])))
        self._upheap(index)
        #logger.debug("UP:UPDATE: %s, %s" %(str(self.index), str(self.data[0:self.size])))
        self._downheap(index)
        #logger.debug("DOWN:UPDATE: %s, %s" %(str(self.index), str(self.data[0:self.size])))

    def update(self, key, item):
        assert item in self.index
        self._update(key, item)

    def add(self, cost, item):
        #logger.debug("ORIG:ADD %s, %s, %d" %(str(self.index), str(self.data), len(self.data)))
        assert len(self.data) >= self.size
        if item not in self.index:
            self.size += 1
            if len(self.data) >= self.size:
                self.data[self.size - 1] = (cost, item)
            else:
                self.data.append((cost, item))
            self.index[item] = self.size - 1
            self._upheap(self.size - 1)
        else:
            self._update(cost, item)
        #logger.debug("ADD %s, %s, %d" %(str(self.index), str(self.data[0:self.size]), self.size))

    def findmin(self):
        if self.size == 0:
            return None, None
        return self.data[0]

    def deleteMin(self):
        #logger.debug("ORIG:REMOVE %s, %s, %d" %(str(self.index), str(self.data[0:self.size]), self.size))
        cost, item = self.data[0]
        assert item in self.index
        del self.index[item]
        if(self.size == 1):
            self.size = 0
        else:
            (lcost, litem) = self.data[self.size - 1]
            self.data[0] = (lcost, litem)
            self.index[litem] = 0 
            self.size = self.size - 1
            self._downheap(0)
        #logger.debug("REMOVE %s, %s, %d" %(str(self.index), str(self.data[0:self.size]), self.size))
        return cost, item

    def check(self):
        for i in range(self.size):
            cost, item = self.data[i]
            assert item in self.index
            assert self.index[item] == i
            if self._parent(i) >= 0:
                assert cost >= self.data[self._parent(i)][0]
            if self._child(i, True) >= 0:
                assert cost <= self.data[self._child(i, True)][0]
            if self._child(i, False) >= 0:
                assert cost <= self.data[self._child(i, False)][0], "%d->%d:%s, %s" %(i, self._child(i, False), str(cost), str(self.data[self._child(i, False)]))
        for key, value in self.index.items():
            assert key == self.data[value][1]

    def __repr__(self):
        return str(self.data[0:self.size])

if __name__ == "__main__":
    h = BinaryHeap()
    N = 100
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
    
