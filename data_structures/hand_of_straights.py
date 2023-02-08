"""
Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.



Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.


Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 109

"""


def group(ilist, k):
    grps = []
    n = len(ilist)
    if n % k != 0:
        print(False)

    from collections import defaultdict
    count = defaultdict(int)

    count = dict()

    for h in ilist:
        if h not in count:
            count[h] = 1
        else:
            count[h] += 1

    count1 = defaultdict(int)

    for h in ilist:
        count1[h] += 1

    for key, value in count1.items():
        cur = key
        for i in range(1, k):

        print(key, value)



    print(count)
    print(count1)

    print(grps)


    return grps


ilist = [1, 6, 3, 3, 4, 4, 5, 2]
output = [[1, 2, 3, 4], [3, 4, 5, 6]]
k = 5
group(ilist, k)










