
"""
in python constructor call mechanism can be changed, like the sequence in which a contructor
is called in inheritance can be changed by calling parent class constructor in inherited class
"""

class A:
    def __init__(self, name):
        self.name = name
        print("my name is A and", self.name)

class B(A):
    def __init__(self, name, age):
        A.__init__(self, name)
        self.name = name
        self.age = age
        print("my name is B and", name)
        print("my age is B and", age)



B("hello", 23)

