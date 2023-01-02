"""
1. self represents the instance of the class
2. Self is always pointing to Current Object.
3. self is the first argument to be passed in Constructor and Instance Method.
4. Self is a convention and not a Python keyword .
"""

# 1
class check_Self_Reference:
    def __init__(self):
        print("address of self = ", id(self))

obj = check_Self_Reference()
print("address of obj = ", id(obj))

obj1 = check_Self_Reference()
print("address of obj1 = ", id(obj1))















