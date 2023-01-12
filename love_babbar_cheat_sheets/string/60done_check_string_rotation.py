"""
60. Write a Code to check whether one string is a rotation of another

Input: S1 = ABCD, S2 = CDAB
Output: Strings are rotations of each other

Input: S1 = ABCD, S2 = ACBD
Output: Strings are not rotations of each other

"""


def check_rotation(s1, s2):

    temp_str = s1 + s1

    if temp_str.count(s2) > 0:
        return 1
    else:
        return 0







S1 = "ABCD"
S2 = "CDAB"

print(check_rotation(S1, S2))













