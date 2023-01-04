"""

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case,
                the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""

# method1: worst approach O(n2)
def max_area_for_water(input_height):
    input_height_length = len(input_height)
    area = 0
    for i in range(input_height_length):
        for j in range(i+1, input_height_length):
            area = max(area, min(input_height[i], input_height[j]) * (j - i))
    return area

# method2: best approach O(n)
def max_area_for_water1(input_height):
    l = 0
    r = len(input_height)-1
    area = 0

    while l < r:
        area = max(area, min(input_height[l], input_height[r]) * (r - l))

        if input_height[l] < input_height[r]:
            l += 1
        else:
            r -= 1
    return area



input_height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(max_area_for_water(input_height))

print(max_area_for_water1(input_height))





















