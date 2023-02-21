from typing import Set


def get_union(list_3, list_5):

    new_list = list_3 + list_5
    for elem in new_list:
        if elem in new_list[(new_list.index(elem) + 1):]:
            new_list.remove(elem)
    # return list(set(list_3).union(set(list_5)))

    return new_list

def get_intersection(list_3, list_5):

    new_list = []
    for elem in list_3:
        if elem in list_5:
            new_list.append(elem)
    return new_list

    # return list(set(list_3).intersection(set(list_5)))

def get_difference(list_3, list_5):

    new_list = []
    # print(list_5)
    for elem in list_3:
        if elem not in list_5:
            # print(elem)
            new_list.append(elem)

    return new_list

    # return list(set(list_3).difference(list_5))

# list_3 = [num*3 for num in range(1, 11)]
# list_5 = [num*5 for num in range(1, 11)]

list_5 = [4,5,7,10,20,30,11,13,20]
list_3 = [7,45,98,34,10,20]


def get_union1(list3, list5):

    union_list = []

    for item in list3:
        if item not in union_list:
            union_list = union_list + [item]
    for item in list5:
        if item not in union_list:
            union_list += [item]

    print(union_list)
    print(set(list3).union(set(list5)))


def get_intersection1(list3, list5):

    intersection_list = []

    for item in list3:
        if item in list5:
            intersection_list += [item]
    print(intersection_list)
    list3 = set(list3)
    list5 = set(list5)
    print(list3.intersection(list5))


def get_difference1(list3, list5):

    diff_list = []
    for item in list3:
        if item not in list5:
            diff_list += [item]

    print(diff_list)
    list3 = set(list3)
    list5 = set(list5)
    print(list3.difference(list5))


print("list3\n", list_3)
print("list5\n", list_5)

# print("intersection\n", get_intersection1(list_3, list_5))
# print("union\n", get_union1(list_3, list_5))
print("get_difference\n", get_difference1(list_3, list_5))


