def merge_two_unsorted_list(l1, l2):
    list3 = l1 + l2

    for i in range(len(list3)):
        for j in range(i + 1, len(list3)):
            if list3[i] > list3[j]:
                list3[i], list3[j] = list3[j], list3[i]

    return list3


input_list1 = [19, 59, 9, 12, 4, 89]
input_list2 = [31, 72, 8, 76, 13, 25, 23, 70, 60]
output_list = [4, 8, 9, 12, 13, 19, 23, 25, 31, 59, 60, 70, 72, 76, 89]

# print(merge_two_unsorted_list(input_list1, input_list2))

def test_merge_two_unsorted_list():
    def merge_two_unsorted_list(l1, l2):
        list3 = l1 + l2
        for i in range(len(list3)):
            for j in range(i + 1, len(list3)):
                if list3[i] > list3[j]:
                    list3[i], list3[j] = list3[j], list3[i]
        return list3

    assert merge_two_unsorted_list(input_list1, input_list2) == output_list