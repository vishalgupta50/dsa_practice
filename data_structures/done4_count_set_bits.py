"""
You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).
N = 4
op = 5
"""

def decimal_to_binary(input_number):
    binary = bin(input_number).replace("0b", "")
    sum = binary.count("1")
    return sum

def count_set_bits(input_number):
    sum = 0
    while input_number > 0:
        sum += decimal_to_binary(input_number)
        input_number -= 1
    return sum

number = 4
print(count_set_bits(number))

# print(decimal_to_binary(number))
