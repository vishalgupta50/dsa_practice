"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""

# worst approach O(n2)
def two_sum(ilist, target):
    for i in range(len(ilist)):
        for j in range(i+1, len(ilist)):
            if ilist[i] + ilist[j] == target:
                return ilist[i], ilist[j]
    else:
        return False



# print all two sum from an array which are not consecuitve
def two_sum1(ilist, target):

    hashmap = {}

    for i in range(len(ilist)):
        temp = target - ilist[i]
        if temp in hashmap:
            print("yes")
            print(temp, ilist[i])
        else:
            hashmap[ilist[i]] = i


# find consecutive sum subarrays whose sum is given sum
def two_sum2(ilist, target):

    hashmap = {}
    olist = []
    for i in range(len(ilist)):
        temp = target - ilist[i]
        if temp in hashmap and ilist[i-1] == temp:
            olist.append([temp, ilist[i]])
            hashmap[ilist[i]] = i
        else:
            hashmap[ilist[i]] = i
    return olist
    # print(hashmap)



ilist = [2, 7, 11, 15, 1, 5, 7, 6, 10, 6, 9, 12, 4, 12]
target = 16

# print(len(ilist))
# print(two_sum(ilist, target))
# print(two_sum1(ilist, target))
print(two_sum2(ilist, target))






