"""

An e-commerce site has a series of advertisements to display. Links to the ads are stored in a data structure and they are displayed or not based on the value
at a bit position in a number. The sequence of ads being displayed at this time can be represented as a binary value, where 1 means the ad is displayed and 0
means it is hidden. The ads should rotate, so on the next page load, ads that are displayed now are hidden and vice versa.

Given a base 10 integer representing the current display state of all ads, determine its binary representation. Starting from the position of its highest
order 1 bit, negate that bit and all lower order bits from 0 to 1 or from 1 to 0. Return the base 10 representation of the result.

Example
base10 = 30

30 10 = 00011110 2

Strip the insignificant zeros then flip all of the bits in 11110 2 to get 000001 2 = 1 10. The example shows the value as an 8-bit binary to demonstrate
that preceding zeros are discarded.

changeAds has the following parameter:
    int base10: an integer in base 10
Return
    int: the base 10 value of resulting binary

Constraints
    0 <= base10 <= 10 to the power 5
Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.


The only line contains a single integer, base10.

Sample Case 0
Sample Input

STDIN    Function
-----    --------
50    →  base10 = 50

Sample Output 0
13

Explanation 0

50 base 10 in binary is 110010 base2. Negate each bit in the sequence to get 001101 base2 = 13 base10.


Sample Case 1
Sample Input
STDIN    Function
-----    --------
100    →  base10 = 100

Sample Output 1
27

Explanation 1

100 base 10 in binary is 1100100 base2. Negate each bit in the sequence to get 0011011 base2 = 27 base10.

"""




# !/bin/python3

# Example: b_n = 100, 2^0*0+2^1*0+2^2*1 = 4
"""
binary number = 100
last bit = 0 2^(index=0)*0
n-1 bit = 0.  2^(index=1)*0
1st bit = 1. 2^(index=2)*1

"""

import math
import os
import random
import re
import sys


#
# Complete the 'changeAds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER base10 as parameter.


def convert_decimal_predefined_function(changeAds):
    def dec_to_binary(base10):
        bin_number = bin(base10).replace("0b", "")
        print("binary number ", bin_number)
        new_num = changeAds(bin_number)
        return new_num
    return dec_to_binary


def convert_decimal_manual_function(changeAds):
    def dec_to_binary(base10):
        print("dec_to_binary initial")
        if base10 >= 1:
            dec_to_binary(base10 // 2)
        base10 = base10 % 2
        print(base10 % 2)
        # print("dec_to_binary after")
        # base10 = base10 % 2
        # print("base10 number ", base10)
        return base10

    return dec_to_binary





# @convert_decimal_predefined_function
@convert_decimal_manual_function
def changeAds(base10):
    '''
    Step 1: convert base10 value to base2 (binary number)
            input: base10=30, output: 11110
    Step 2: base2 value flip each bit of this number base
            input: base2=11110 output: 00001
    Step 3: calculate corresponding base10 value from flip bit
            input base2=00001 output=1 (base10)
    '''

    base10 = list(base10)
    for i in range(len(base10)):
        if base10[i] == '0':
            base10[i] = '1'
        else:
            base10[i] = '0'

    new_num = "".join(str(elem) for elem in base10)
    print("changed number ", new_num)
    return new_num









x = changeAds(100)

print("chnaged ads ", x)

# print(bin(50))

# print(11//5)




# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     base10 = int(input().strip())
#
#     result = changeAds(base10)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()



























