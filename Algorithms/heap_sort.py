# Heapify
# Time = O(n), space : O(1)
# Heap push - Insertion
# Heap pop (extract min)

# heap sort
# Time : O(nlogn), space O(n)
import heapq
def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0]*n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    
    return new_list

