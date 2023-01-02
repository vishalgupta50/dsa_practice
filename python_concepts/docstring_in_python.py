
def print_hello():
    """
    This function returns string hello
    Returns: "hello

    """
    return "hello"


print(print_hello.__doc__) # returns the docs of the function
print(print_hello)
print(print_hello())

print(print_hello.__name__) # returns the name of the function
print(print_hello.__code__)








