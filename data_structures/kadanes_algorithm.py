"""
Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

Example 1:
Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which
is a contiguous subarray.

Example 2:
Input:
N = 4
Arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1
of element (-1)

Your Task:
You don't need to read input or print anything. The task is to complete the function maxSubarraySum() which takes Arr[]
and N as input parameters and returns the sum of subarray with maximum sum.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 106
-107 ≤ A[i] ≤ 107

NOTE: Kadane’s Algorithm can be viewed both as greedy and DP. As we can see that we are keeping a running sum of integers and when
it becomes less than 0, we reset it to 0 (Greedy Part). This is because continuing with a negative sum is way worse than restarting
with a new range. Now it can also be viewed as a DP, at each stage we have 2 choices: Either take the current element and continue
with the previous sum OR restart a new range. Both choices are being taken care of in the implementation.

"""

arr = [-2, -3, 4, -1, -2, 1, 5, -3]

def maxSubArraySum(arr):

    len_arr = len(arr)


    return []



print(maxSubArraySum(arr))










