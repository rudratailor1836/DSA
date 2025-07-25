import time

def selection_sort(arr):
    # we need to loop for number of passes
    for i in range(len(arr)-1):
        min = i # here pass means the first index object
        for j in range(i + 1,len(arr)):
            # this will check and change min value accordingly
            if arr[j] < arr[min]:
                min = j
        # swapping items 
        arr[i],arr[min] = arr[min],arr[i]
        time.sleep(0.25)
        print(arr)
        


arr = [0,1,2,3,4,5,6,7,8,9]

# arr = [6,8,7,4,5,1,9,3,2,0]

selection_sort(arr)