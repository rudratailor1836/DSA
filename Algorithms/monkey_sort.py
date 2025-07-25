# Monkey Sorting systum

import random
import time

def is_sorted(arr):
    sorted = True

    for i in range(len(arr)-1):
        if arr[i]> arr[i+1]:
            sorted = False
    
    return sorted


def monkey_sort(arr):
    while not is_sorted(arr):
        # time.sleep(1)
        random.shuffle(arr)
        print(arr)
    print(arr)

a = [12, 45 ,1,23,4,67,21,11,112]

monkey_sort(a)