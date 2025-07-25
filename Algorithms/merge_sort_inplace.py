def merge_sorted(arr1,arr2,arr):
    i = j = k =  0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i+=1
        else:
            arr[k] = arr2[j]

            j+=1
        k += 1
        
    while i < len(arr1):
        arr[k] = arr1[i]
        i+=1
        k +=1
    while j < len(arr2):
        arr[k] = arr2[j]
        j+=1
        k += 1

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

    merge_sorted(left,right,arr)

    return arr


arr = [23,546,3,2,66,33,77,32,12,6,0,4,1]

print(merge_sort(arr))