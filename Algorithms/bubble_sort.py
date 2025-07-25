import time

def bubble_sort(arr):
    for i in range(len(arr)-1):
        flag = 0
        for j in range(len(arr)-1- i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = 1
        time.sleep(0.25)
        print(arr)
        if flag == 0:
            break
        
    
     
                
    
arr= [9,56,344,76,4,3,676,5,78,12,1,0,56,33,5,32,2]

bubble_sort(arr)