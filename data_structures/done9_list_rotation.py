"""
rotate the list with n number/rotation
"""


input_list = [10, 20, 30, 40, 50, 60, 90, 80]
rotation_number = 3

# method by creating new list and using loops O(n)
def rotate_list(i_list, r_number):
    n = len(input_list)
    output_list = []

    for i in range(n-r_number, n):
        output_list.append(input_list[i])
    for i in range(0, n-r_number):
        output_list.append(input_list[i])

    return output_list


def rotate_list1(i_list, r_number):
    i_list = i_list[-r_number:] + i_list[:-r_number]
    return i_list

def rotate_list2(i_list, r_number):


    return []


print(rotate_list(input_list, rotation_number))

print(rotate_list1(input_list, rotation_number))

print(rotate_list2(input_list, rotation_number))



