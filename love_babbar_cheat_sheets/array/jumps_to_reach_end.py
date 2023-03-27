"""
Minimum no. of Jumps to reach end of an array

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 9 -> 9)
Explanation: Jump from 1st element to 2nd element as there is only 1 step.
Now there are three options 5, 8 or 9. I
f 8 or 9 is chosen then the end node 9 can be reached. So 3 jumps are made.

Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
Output: 10
Explanation: In every step a jump is needed so the count of jumps is 10.

low = 0
index = 0

while low <= len(arr)
    maximum = max(arr[arr.index(low):arr.index(low+1)]
    if max > len(range(arr[arr.index(low):arr.index(low+1)))

        jump = jump+1
    else:
        low = arr.index(max)
    jump += 1
"""



def min_jumps(arr):
    low = 0
    jump = 0
    while low <= len(arr):
        sub_arr = arr[low:arr.index(arr[low+1])]
        maximum = max(sub_arr)
        a = len(range(sub_arr))
        if maximum > len(range(arr.index())):
            jump = jump + 1
            break
        else:
            low = arr.index(max)
        jump = jump + 1

    print(arr)


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
min_jumps(arr)

var = arr[3:5]
print(var)
print(arr.index(9), type(arr.index(9)))



