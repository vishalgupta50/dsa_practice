"""

find an element in sorted list using binary search


"""



def binary_search(arr, low, high, key):


    mid = low + (high-low) // 2
    # print(mid)

    if key == arr[mid]:
        print(mid)

    elif key < arr[mid]:
        binary_search(arr, low, mid-1, key)
    else:
        binary_search(arr, mid+1, high, key)




arr = [3, 5, 6, 7, 9, 10, 12, 23, 25, 27, 30, 32, 35]

low = 0
high = len(arr)-1
key = 32

binary_search(arr, low, high, key)










