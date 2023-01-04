"""
convert decimal to binary
"""

# using recursion
def decimal_to_binary(input_number):
    if input_number >= 1:
        decimal_to_binary(input_number // 2)
    print(input_number % 2, end='')


# using while loop
def decimal_to_binary1(input_number):

    dec_list = ""
    while input_number > 0:
        dec_list = dec_list + str(input_number % 2)
        input_number = input_number // 2

    return dec_list[::-1]
    # return "".join(reversed(dec_list))

# using pre-defined function
def decimal_to_binary2(input_number):
    binary_number = bin(input_number).replace("0b", "")
    return binary_number




number = 44
print(decimal_to_binary1(number))

print(int(decimal_to_binary1(number)))

print(decimal_to_binary2(number))


