# Linear searching based on brute force

def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
        
    return "Item Not Found"

arr = [1,34,22,44,232,455,33,22,55,33,22,44,322,121,34,55,33,22,3,33,22,33,232,12,22,33,3,1]

print(linear_search(arr,3))