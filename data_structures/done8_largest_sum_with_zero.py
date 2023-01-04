"""
input_list = [15,-2,2,-8,1,7,10,23]
find largest subarray with sum 0
"""



input_arr = [15,-2,2,-8,1,7,10,23, -5, 5, -23, -18]


def find_largest_zero_sublist(input_list):
    sum = 0
    dic = {}

    for i in range(len(input_list)):

        sum = sum + input_list[i]
        if sum not in dic:
            dic[sum] = i
        else:
            max_len = i - dic[sum]

    return max_len

print(find_largest_zero_sublist(input_arr))

