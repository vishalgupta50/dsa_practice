"""
Move all the negative elements to one side of the array
"""

def move_negative_to_left1(arr):

    low = 0
    high = len(arr) - 1

    while low < high:
        if arr[low] < 0 and arr[high] < 0:
            low += 1
        if arr[low] > 0 and arr[high] > 0:
            high -= 1
        elif arr[low] < 0 and arr[high] > 0:
            low += 1
            high -= 1
        elif arr[low] > 0 and arr[high] < 0:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    print(arr)


def move_negative_to_left2(arr):

    itr = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[itr] = arr[itr], arr[i]
            itr += 1

    print(arr)









arr = [5, 8, -2, 4, 8, -9, -2, 7, 3, -4]
move_negative_to_left2(arr)



