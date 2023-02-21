"""
Find the "Kth" max and min element of an array
"""

def find_kth_min_max(arr, k):
    min, max = 0, 0
    freq_dict = {}

    for elem in arr:
        if elem in freq_dict:
            freq_dict[elem] += 1
        else:
            freq_dict[elem] = 1
    print(freq_dict)

    min_kth = 0
    max_kth = 0
    for itr in sorted(freq_dict.keys()):
        min_kth += freq_dict[itr]
        if min_kth == k:
            print(itr)

    sorted(freq_dict.keys())
    print(freq_dict)

    print(freq_dict)


    return min, max



arr = [12, 3, 5, 7, 7, 19]
k = 2
find_kth_min_max(arr, k)