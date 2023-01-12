"""
Input : s = "GeeksforGeeks"
        d = 2
Output : Left Rotation  : "eksforGeeksGe"
         Right Rotation : "ksGeeksforGee"


Input : s = "qwertyu"
        d = 2
Output : Left rotation : "ertyuqw"
         Right rotation : "yuqwert"

"""


def rotate_string_left_and_right(string, d):
    n = len(string)
    left_rotate = string[n-d:] + string[:n-d]
    right_rotate = string[d:n] + string[:d]
    return left_rotate, right_rotate




s = "GeeksforGeeks"
d = 2
print(rotate_string_left_and_right(s, d))



