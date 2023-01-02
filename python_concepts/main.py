# # This is a sample Python script.
# 
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# import unittest
# 
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
# 
# 
# # Press the green button in the gutter to run the script.
# class CheckPalindrom:
#     pass
# 
# 
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     CheckPalindrom.run()
# 
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# 
# 
# 
# 
# def get_input_from_user():
#     s = 1234321
#     return s
# 
# def check_palindrome(input):
#     # cheking palindrome
#     new_s = 0
#     while input >= 0:
#         s = input % 10
#         new_s = new_s * 10 + s
#         input = input / 10
#     if new_s == input:
#         return True
#     else:
#         return False
#     
#     
# 1234
# s = 3
# new_s = 4321
# input = 12
# 
# 
# s
# 
# 
# def setup():
#     print("setup")
# 
# def teardown():
#     print("teardown")
# 
# class CheckPalindrom(unittest.TestCase):
#     
#     def run(self):
#         s = get_input_from_user()
#         check = check_palindrome(s)
#         assert True, check
#         
# 
# 
# 
# 
# 
# var =1
# execute func1
# var = 2 
# execure func2
# 

def execute_func1():
    print("func1")


def execute_func2():
    print("func2")


def execute_func3():
    print("func3")

# s = execute_func1()


var = 1
value = {var == 1: execute_func1(), var == 2: execute_func2()}.get(True, execute_func3())

print(value)
