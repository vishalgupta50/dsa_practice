"""
Given an array of integers. Find the Inversion Count in the array.
[2, 4, 1, 3, 5]
op  3

Array: {1,5,2, 8,3,4}
Pairs: {5, 2}, {5, 3}, {5, 4}, {8, 3}, {8, 4}
Output: 5

Array: { 5, 4, 3, 2, 1} // reverse Order
Pairs: {5, 4}, {5,3, {3,2}, {3,1}, {2,1},{4,3}, {4,2}, {4,1},}, {5,2}, {5,1}
Output: 10

"""

input_list = [1,5,2, 8,3,4]

# worst approach O(n2)
def inversion_count(input_list):
    invert_count_list = []
    input_list_len = len(input_list)
    invert_count = 0
    for i in range(input_list_len):
        for j in range(i+1, input_list_len):
            if input_list[i] > input_list[j]:
                invert_count_list.append([input_list[i], input_list[j]])
                invert_count += 1
    return invert_count_list, invert_count


# normal approach using merge sort O(nlogn)
# can be done using merge sort and (heap sort + bisection)
def inversion_count1(input_list):
    invert_count_list = []
    input_list_len = len(input_list)
    # j = 1
    # for i in range(input_list_len):
    #     if




print(inversion_count(input_list))
# print(type(inversion_count(input_list)))

for index, value in enumerate(input_list):
    print(index, value)





