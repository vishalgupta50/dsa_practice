"""
IP: 421
OP: 491
Explanation : 4+2+1+42+21+421
IP: 123
OP: 164
Explanation : 1+2+3+12+23+123

IN:1234
OP:1670
1+2+3+4+12+23+34+123+234+1234

IP and OP are in string format.
"""

"""
[4, 2, 1, 42, 21, 421]





"""


# input_number = "421"
input_number = "1234"

def add_elements_of_number(input_str):

    sum = 0
    new_list = []
    for i in range(len(input_str)):
        for j in range(i + 1, len(input_str) + 1):
            sum = sum + int(input_str[i:j])
            new_list.append(input_str[i:j])
    print(new_list)
    return sum

print(add_elements_of_number(input_number))












