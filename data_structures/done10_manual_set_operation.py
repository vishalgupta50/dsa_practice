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

list_3 = [num*3 for num in range(1, 11)]
list_5 = [num*5 for num in range(1, 11)]

# list_5 = [4,5,7,10,20,30,11,13]
# list_3 = [7,45,98,34,10,20]

print("list3\n", list_3)
print("list5\n", list_5)

print("intersection\n", get_intersection(list_3, list_5))
print("union\n", get_union(list_3, list_5))
print("get_difference\n", get_difference(list_3, list_5))


