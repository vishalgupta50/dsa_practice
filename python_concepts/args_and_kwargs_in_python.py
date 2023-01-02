"""
*args = non keyword arguments
**kwargs = keyword arguments

Note: “We use the “wildcard” or “*” notation like this – *args OR **kwargs – as our
function’s argument when we have doubts about the number of  arguments we should pass in a function.”

"""

def myFunc(arg, *argv):
    print("first argument ", arg)
    for arg in argv:
        print(arg)

myFunc("hello", 20, ["a", 2])



def myFunc1(arg, **kwargs):
    for key, value in kwargs.items():
        print("key is ", key, "value is ", value)

myFunc1( "hello" , first = "geek", low = "hello", abcd = "why")










