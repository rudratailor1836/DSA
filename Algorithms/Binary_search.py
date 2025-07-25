# Binary search
# in this we need to divide the sorted array into 2 parts and see if number is less than the half greater part will be removed and vice verse 

# through recursion
def binary_search(arr,low, high, item):
    if low <= high:
        # search
        mid = (low + high)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search(arr, low, mid-1, item)
        else:
            return binary_search(arr, mid + 1, high, item)
    else:
        return "Item Not Found"
    


# Through Loops

def binarySearch(arr,target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found


arr = [12,23,34,45,56,67,78,89,90,100,123]

print(binary_search(arr,0, len(arr)-1, 78))
print(binarySearch(arr,78))
    