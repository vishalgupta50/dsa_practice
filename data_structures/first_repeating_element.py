"""
Given an array arr[] of size n, find the first repeating element. The element should occur more than once and the index of its first
occurrence should be the smallest.

Note:- The position you return should be according to 1-based indexing.

Example 1:

Input:
n = 7
arr[] = {1, 5, 3, 4, 3, 5, 6}
Output: 2
Explanation:
5 is appearing twice and
its first appearence is at index 2
which is less than 3 whose first
occuring index is 3.

Example 2:

Input:
n = 4
arr[] = {1, 2, 3, 4}
Output: -1
Explanation:
All elements appear only once so
answer is -1.

Your Task:
You don't need to read input or print anything. Complete the function firstRepeated() which takes arr and n as input parameters
and returns the position of the first repeating element. If there is no such element, return -1.


Expected Time Complexity: O(n)
Expected Auxilliary Space: O(n)



Constraints:
1 <= n <= 106
0 <= Ai<= 106
"""

# more time taking
# def first_repeating(input_list):
#
#     for i in range(len(input_list)):
#         if input_list[i] in input_list[(i + 1):]:
#             return input_list[i]
#     else:
#         return -1


def first_repeating(input_list):

    sample_dict = {}
    for i in range(len(input_list)):
        if input_list[i] in sample_dict:
            sample_dict[input_list[i]] += 1
        else:
            sample_dict[input_list[i]] = 1
    print(sample_dict)

    for i in range(len(input_list)):
        if sample_dict[input_list[i]] > 1:
            return i + 1

    return -1


input_list = [1, 7, 8, 4, 3, 5, 6, 23, 4, 3]
first_repeated_element = first_repeating(input_list)
print(first_repeated_element)













