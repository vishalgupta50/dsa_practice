

def merge_two_sorted_list(l1, l2):

    list3 = l1 + l2

    for i in range(len(list3)):
        for j in range(i+1, len(list3)):
            if list3[i] > list3[j]:
                list3[i], list3[j] = list3[j], list3[i]


    return list3



input_list1 = [4, 5, 9, 12, 34, 89]
input_list2 = [3, 7, 8, 10, 12, 20, 23, 45, 60]

print(merge_two_sorted_list(input_list1, input_list2))