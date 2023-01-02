"""
separate odd and even without creating a new list
int a[] ={7, 2, 4, 1, 3, 5, 6, 8, 2, 10};


input_list_number = [7, 2, 4, 1, 3, 5, 6, 8, 2, 10]

output_list_number = [2, 4, 6, 8, 2, 10, 7, 1, 3, 5]
"""

input_list_number = [7, 2, 4, 1, 3, 5, 6, 8, 2, 10, 11]

output_list_number = [2, 4, 6, 8, 2, 10, 7, 1, 3, 5]


# O(n2)
def swap(input_list, index1, index2):
    temp = input_list[index1]
    input_list[index1] = input_list[index2]
    input_list[index2] = temp

# def separate_even_odd(input_list):
#
#     for i in range(len((input_list))//2 + 1):
#         if input_list[i] % 2 != 0:
#             for j in range(i+1, len(input_list)):
#                 if input_list[j] % 2 == 0:
#                     swap(input_list, i, j)
#                     # temp = input_list[j]
#                     # input_list[j] = input_list[i]
#                     # input_list[i] = temp
#
#     return input_list


def separate_even_odd(input_list):
    i = 0
    j = len(input_list) - 1

    while i <= j:
        if input_list[i] % 2 != 0:
            if input_list[j] % 2 == 0:
                input_list[i], input_list[j] = input_list[j], input_list[i]
                i += 1
            j -= 1
        if input_list[i] % 2 == 0:
            i += 1

    return input_list






print(separate_even_odd(input_list_number))














