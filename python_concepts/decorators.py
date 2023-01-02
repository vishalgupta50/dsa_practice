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











