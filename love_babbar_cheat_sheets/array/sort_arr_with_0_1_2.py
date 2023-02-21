"""
Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
"""

def sortarr012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    print(arr)








arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sortarr012(arr)

