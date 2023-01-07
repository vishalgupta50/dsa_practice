"""
sort the sentence by using the weight if the individual word
string = my name is john

my =
name =
is =
john =


"""

string1 = "my name is john"
# str.lowercase.index('b')

# print(str.lower('b').index('b'))
#
# print(str.index('a'))

# print(ord("m"))
# print(ord("y"))

def sort_by_weight(str1):
    # str1 = str1.split()
    print(str1)
    word = ""
    sum = 0
    list1 = []
    for char in str1 + " ":
        if char != " ":
            word = word + char
            sum += ord(char) - 96
        else:
            list1.append((word, sum))
            word = ""
            sum = 0

    list1.sort(key=lambda x: x[1])
    for elem in list1:
        word += elem[0] + " "

    print(word.rstrip())
    print(list1)
    # for elem in list1:


    print(list1)
    return ""

def sort_by_weight1(str1):
    str1 = str1.split()
    sum = 0
    list1 = []
    for elem in str1:
        for char in elem:
            sum += ord(char) - 96
        list1.append((elem, sum))
        sum = 0
    list1.sort(key= lambda x: x[1])
    str1 = ""
    for elem in list1:
        str1 += elem[0] + " "
    return str1.rstrip()


print(sort_by_weight(string1))
# print(sort_by_weight1(string1))

# print(ord("c")-96)