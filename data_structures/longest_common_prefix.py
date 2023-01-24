"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


def longest_common_prefix(strs):

    str1 = strs[0]
    temp_str = ""
    count = 0
    dict1 = dict()

    for char in strs[0]:
        dict1[char] += 1



    print("temp_str = ", temp_str)





strs = ["flower","flow","flight"]
longest_common_prefix(strs)





