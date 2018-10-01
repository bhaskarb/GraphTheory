#Implement a heap
import random

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
        if i == 0 or self.size == 0:
            return -1
        return i/2

    def _child(self, i, left=True):
        if self.size == 0:
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
        #print ci, ckey, citem
        if li >=0 and ri >=0:
            lkey, litem = self.data[li]
            rkey, ritem = self.data[ri]
            #print li, lkey, litem
            #print ri, rkey, ritem
            if lkey < ckey and lkey <= rkey:
                mi, mkey, mitem = li, lkey, litem
            elif rkey < ckey and rkey  < lkey:
                mi, mkey, mitem = ri, rkey, ritem
        elif li >=0:
            lkey, litem = self.data[li]
            #print li, lkey, litem
            if lkey < ckey:
                mi, mkey, mitem = li, lkey, litem
        elif ri >=0:
            rkey, ritem = self.data[ri]
            #print ri, rkey, ritem
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
            if ckey < pkey:
                self.data[pi] = ckey, citem
                self.data[ci] = pkey, pitem
                self.index[pitem] = ci
                self.index[citem] = pi
                self._upheap(pi)

    def _update(self, key, item):
        print self.index
        index = self.index[item]
        self.data[index] = (key, item)
        self._upheap(index)
        self._downheap(index)

    def update(self, key, item):
        assert item in self.index
        self._update(key, item)

    def add(self, cost, item):
        if item not in self.index:
            self.index[item] = self.size
            if len(self.data) <= self.size:
                self.data.append((cost, item))
            else:
                self.data[self.size - 1] = (cost, item)
            self._upheap(self.size)
            self.size += 1
        else:
            self._update(key, item)
        print "ADD %s, %s, %d" %(str(self.index), str(self.data), self.size)

    def findmin(self):
        if self.size == 0:
            return None, None
        return self.data[0]

    def deleteMin(self):
        cost, item = self.data[0]
        del self.index[item]
        if(self.size == 1):
            self.size = 0
        else:
            self.data[0] = self.data[self.size - 1]
            self.size = self.size - 1
            #print self.data[0:self.size]
            self._downheap(0)
        print "REMOVE %s, %s, %d" %(str(self.index), str(self.data), self.size)
        return cost, item

if __name__ == "__main__":
    h = BinaryHeap()
    N = 100000
    items = [random.randint(1, 1000) for i in range(N)]
    i = 0
    for item in items:
        h.add(item, i)
        i = i + 1
    prevkey = None
    while not h.empty():
        newkey = h.remove()
        assert prevkey == None or prevkey <= newkey
        #print h.data[0:h.size]
