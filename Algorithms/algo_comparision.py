import random
import time


def bubble_sort(arr):
    start = time.time()
    for i in range(len(arr)-1):
        flag = 0
        for j in range(len(arr)-1- i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = 1
        
        if flag == 0:
            break
    # print(arr)
    print("Time" , time.time()- start, "sec")

def selection_sort(arr):
    start = time.time()

    # we need to loop for number of passes
    for i in range(len(arr)-1):
        min = i # here pass means the first index object
        for j in range(i + 1,len(arr)):
            # this will check and change min value accordingly
            if arr[j] < arr[min]:
                min = j
        # swapping items 
        arr[i],arr[min] = arr[min],arr[i]

    # print(arr)
    print("Time" , time.time()- start, "sec")

def merge_sorted(arr1,arr2):
    i = j = 0

    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
        
    while i < len(arr1):
        merged.append(arr1[i])
        i+=1
    while j < len(arr2):
        merged.append(arr2[j])
        j+=1

    return merged

# a = [1,3,5]
# b = [2,4,6]

# print(merge_sorted(a,b))

def merge_sort(arr):
    
    if len(arr) == 1:
        return arr
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_sorted(left,right)



# arr = [23,546,3,2,66,33,77,32,12,6,0,4,1]

# print(merge_sort(arr))

l = []
for i in range(10000):
    l.append(random.randint(1,10000))

L1 = l[:]
L2= l[:]
L3 = l[:]

bubble_sort(L1)
selection_sort(L2)
start = time.time()
print(merge_sort(L3))
print("Time",time.time() - start, 'sec' )

# selection sort is faster