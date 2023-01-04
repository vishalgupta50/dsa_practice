"""
Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to
a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which comes first on moving from left to right.

Note:- Both the indexes in the array should be according to 1-based indexing. You have to return an arraylist consisting
of two elements left and right. In case no such subarray exists return an array consisting of element -1


Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements
from 2nd position to 4th position
is 12.

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements
from 1st position to 5th position
is 15.

"""


# worst approach
def subArraySum(arr_list):
    index_list = []
    for i in range(len(arr_list)):
        count = arr_list[i]
        if arr_list[i] == 15:
            index_list.append([i + 1, i + 1])
        for j in range(i+1, len(arr_list)):
            # print(i, " ", j)
            count += arr_list[j]
            if count == 15:
                index_list.append([i+1, j+1])

    return index_list




arr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 98, 15, 45, 15, 0, 10, 5, 8, 8, -1]


print(subArraySum(arr_list))