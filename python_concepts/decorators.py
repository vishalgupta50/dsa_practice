"""

"""

def check_distinction(result_function):
    def distinction(marks):
        for m in marks:
            if m >= 75:
                print("DISTINCTION")
        result_function(marks)
    return distinction


@check_distinction
def result(marks):
    for m in marks:
        if m >= 33:
            pass
        else:
            print("FAIL")
            break
    else:
        print("PASS")


result([33, 45, 90, 100, 67])



def decorate_vishal(func):
    def decorating():
        print("Before decorating")
        func()
        print("after decorating")
    return decorating()


@decorate_vishal
def who_is_vishal():
    print("I am vishal")




def deocrate_divide(func):
    def divide_by_zero(a, b):
        if b == 0:
            b += 2
        return func(a, b)
    return divide_by_zero




@deocrate_divide
def divide(a,b):
    return int(a)/int(b)


print(divide(6, 0))



# decorator that adds some elements in sum function


def add_element(func):
    def wrapper(x, y):
        x += 2
        y += 2
        return func(x, y)
    return wrapper


@add_element
def add(x, y):
    return x + y


print(add(3,2))






























