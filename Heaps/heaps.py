
class MinHeap:

    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

    def insert(self, key , value):
        self.heap.append((key,value))
        self._sift_up(len(self.heap)-1)
    def peek_min(self):
        if not self.heap:
            raise IndexError("Empty Heap")
        return self.heap[0]


    def extract_min(self):
        if not self.heap:
            raise IndexError("Empty Heap")
        min_element = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)

        return min_element

    def heapify(self, elements):
        self.heap = list(elements)

        for i in reversed(range(self._parent(len(self.heap)-1)+1)):
            self._sift_down(i)

    def meld(self, other_heap):
        if not isinstance(other_heap, MinHeap):
            raise TypeError("Expected a MinHeap instance")
        combined_heap = self.heap + other_heap
        self.heapify(combined_heap)
        
    def _parent(self,index):
        return (index - 1) // 2 if index > 0 else None
    
    def _left(self, index):
        left = 2*index + 1
        return left if left < len(self.heap) else None

    def _right(self, index):
        right = 2*index + 2
        return right if right < len(self.heap) else None
    def _sift_up(self, index):
        # swim operation
        parent_index = self._parent(index)

        while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)
        

    def _sift_down(self,index):
        # sink operation
        while True:
            smallest = index
            left = self._left(index)
            right = self._right(index)

            if left is not None and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left

            if right is not None and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            
            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def is_empty(self):
        return len(self.heap) == 0

X = MinHeap()

import random
arr= [9,7,6,5,3,2,1,0,-10]

for i in arr:
    string = str(i)
    X.insert(i,string)

print(X)