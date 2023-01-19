"""
Input: exp = “[()]{}{[()()]()}”
Output: Balanced
Explanation: all the brackets are well-formed

Input: exp = “[(])”
Output: Not Balanced
Explanation: 1 and 4 brackets are not balanced because
there is a closing ‘]’ before the closing ‘(‘

"""



# used two different kind of data structures list and dictionary
def check_balance_paranthese1(istr):
    # print(input_str)

    bal_dict = {"{": 0, "[": 0, "(": 0}

    for char in istr:
        # print(type(char), char)
        if char in ["{", "(", "["]:
            bal_dict[char] += 1
        elif char == "}":
            bal_dict["{"] -= 1
        elif char == ")":
            bal_dict["("] -= 1
        elif char == "]":
            bal_dict["["] -= 1
        else:
            bal_dict[char] = -1

    # print(bal_dict)

    for key, value in bal_dict.items():
        # print(elem)
        print(key, value)
        if value >= 1 and key in ["{", "(", "[", "]", ")", "}"]:
            return False
    return True

    # return True


# using stacks
def check_balance_paranthese(istr):
    stack = []

    # Traversing the Expression
    for char in istr:
        if char in ["(", "{", "["]:

            # Push the element in the stack
            stack.append(char)
        else:

            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True

def check_balance_paranthese2(test_str):
    if len(test_str) % 2 != 0:
        return False
        # initialize parentheses dict
    par_dict = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in test_str:
        # push opening bracket to stack
        if char in par_dict.keys():
            stack.append(char)
        else:
            # closing bracket without matching opening bracket
            if stack == []:
                return False
            # if closing bracket -> pop stack top
            open_brac = stack.pop()
            # not matching bracket -> invalid!
            if char != par_dict[open_brac]:
                return False
    return stack == []


def check_balance_paranthese3(my_string):
    brackets = ['()', '{}', '[]']
    while any(x in my_string for x in brackets):
        for br in brackets:
            my_string = my_string.replace(br, '')
    return not my_string




input_str = '}{}{'

print(check_balance_paranthese3(input_str))




















