# stri = "abcd sdf sdfs"
# print(stri[1])
#
# print(ord('a') - 96)
#
# # for i in stri:
# #     print(i)
#
#
# x = [3, 4, 89, 21]
# print(x, id(x))
#
# y = list(x)
# print(y, id(y))
# y[3] = 32
#
# x.sort()
# print(x, id(x))
#
# print(y, id(y))
#
#
#
# str1 = "abcd "
# print(str1, id(str1))
#
# str2 = str1.rstrip()
# print(str2, id(str2))
# print(str1, id(str1))
#
#
# x = [67, 23, 90, 2, 1, 45]
# print(x, id(x))
# x.sort()
# # sorted(x)
# print(x, id(x))
#
# y = [89, 45, 90, 67, 23, 88]
# print(y, id(y))
# z = sorted(y)
# print(z, id(z))
#
#
#
#
# bal_dict = {
#     "[": 1,
#     "{": 2
# }
# print(bal_dict)
#
# char = "("
# bal_dict[char] = 5
#
# print(bal_dict)
#
#
# for key, value in bal_dict.items():
#     print(key, value)
#
# y = [89, 45, 90, 67, 23, 88]
# print(y)
# print(y.pop(0))
# print(y)
# print(id(y))
# y.sort()
# print(id(y))
#
#
# number = 1234
# print(len(str(number)))
# print(number%10000)
# print(number%1000)
# print(number%100)
# print(number%10)
# number = number//10
# # print(number)
# print(number%1000)
# print(number%100)
# print(number%10)
# # print(number%10)
# number = number //10
# print(number%100)
# print(number%10)
# number = number // 10
# print(number%10)
# print(number)
#
#
# tup = ()
# print(type(tup))
#
# for i in range(1, 3):
#     # print(i)
#     for j in range(4, 10):
#         # print(j)
#         if j == 6:
#             break
#         else:
#             print(j)

# input = "1234"
#
# print(input[0:1])
#
#
# list1 = [10, 20, 30, 4, 25, 70, 4, 1, 99, 60]
# # list1 = [10, 20, 5]
#
# def second_largest(list1):
#     max1 = float('-inf')
#     max2 = float('-inf')
#     print(max1, max2, type(max1))
#     for item in list1:
#         if item > max1:
#             max2 = max1
#             max1 = item
#         elif item > max2 and item < max1:
#             max2 = item
#     print(max2)
#
#
# second_largest(list1)

#
# x = 10
# y = 10
# print(id(x), id(y))
#
#
# class Employee:
#     def __init__(self, ename):
#         self.ename1 = ename
#
#
# class Company(Employee):
#     def __init__(self, ename, cname):
#         super().__init__(ename)
#         self.cname = cname
#
#     def display(self):
#         print(self.ename1, self.cname)
#
#
# c = Company("vishal", "prog_comp")
#
# c.display()


# import unittest
#
#
# def remove_extras(func):
#     def remove(str1, x):
#         new_sentence = ""
#         for char in str1:
#             if char not in [",", " ", ":"]:
#                 new_sentence += char.lower()
#         return func(str1, 5)
#     return remove
#
# @remove_extras
# def isPalidrome(str1, n):
#     return str1 == str1[::-1]
#
#
# class TestIsPalindrome(unittest.TestCase):
#     test_string = "abcd Hello"
#     test_length = 30
#
#     def test_palindrome(self):
#         self.assertFalse(isPalidrome(self.test_string, self.test_length))


# s = "A man, a plan, a canal: Panama"
# s = "a abs ghj jhg sba a"
# print(isPalidrome(s, 5))

#
#
#
# dic = {
#     "emp1": {
#         "name": "vishal",
#         "age": 45,
#     },
#     "emp2": {
#         "name": "xyz"
#     }
#
# }
#
# print(dic)


# for i in range(1, 10):
#     print(i)
#     # i += 2

a = [34, 56, 23, 67, 12, 90, 12]
print(a[3:])
print(a[:3])
print(len(a))



