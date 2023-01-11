"""

Given an integer N, the task is to find the number of ways to represent this number as a sum of 2 or more consecutive

Example 1:
Input: n = 5
Output: 2
Explanation: 5 = 2 + 3

Example 2:
Input: n = 9
Output: 3
Explanation: 9 = 4 + 5 = 2 + 3 + 4

Example 3:
Input: n = 15
Output: 4
Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

"""


# bruteForce approach O(n2)
def find_consecutive_sum(number):

    # n = len(number)
    count = 0
    list1 = []
    for start in range(1, number-1):
        end = start + 1
        sum = start + end
        while sum < number:
            end += 1
            sum += end
            list1.append(sum)
        if sum == number:
            count += 1
    return count


# prefix sum method O(sqrt n) auxilary space: O(n)
def find_consecutive_sum1(number):
    prefix_sum_list = [0]
    for i in range(1, number):
        prefix_sum_list.append(prefix_sum_list[i-1]+i)

    count = 0
    for ele in prefix_sum_list:
        if ele-number in prefix_sum_list:
            count += 1
    return count



# prefix sum method O(sqrt n) auxilary space: O(1)
"""
                                    15
1+2+3+4+5                           4+5+6                      7+8
a = 1                              a = 4                    a = 7
a+(a+1)+(a+2)+(a+3)+(a+4)          a+(a+1)+(a+1)                  a+(a+1)
L = 4                              L = 1                    L = 1

number = a+(a+1)+(a+2)+(a+3)+(a+4).......(a+L)
take L+1 separate which can be multiplied by a and 1+2+3+4....L will be left out which can be written as
number = (L+1)*a + (1+2+3+4.....+L) which can be further written as
number = (L+1)*a + L(L+1)/2 
now to get the value of a

a = (number - L(L+1)/2)/(L+1)

now
number = 15, L = 1
a = (15 - 1(1+1)/2)/(1+1)
a = 7
now we know that sequence is a + (a+1) so the sequence can be 7 + 8 = 15

number = 15, L = 2
a = (15 - 2(2+1)/2)/(2+1)
a = 4
now we know that sequence is a+(a+1)+(a+2) so the sequence can be 4 + 5 + 6 = 15

number = 15, L = 3
a = (15 - 3(3+1)/2)/(3+1)
a = 2.25
we can't take non integer value because that will give us nothing

number = 15, L = 4
a = (15 - 4(4+1)/2)/(4+1)
a = 1
now we know that sequence is a+(a+1)+(a+2)+(a+3)+(a+4) so the sequence can be 1 + 2 + 3 + 4 + 5 = 15


MAXIMUM LENGTH OF CHAIN
the maximum lenght of chain can be max number which starts from 1 for eg:
1 + 2 + 3 + 4 + 5 so max length can be 5 only

Hurray!!!! Let's solve this now
"""

def find_consecutive_sum2(number):
    count = 0
    chain_length = 0
    sum = 0
    while sum < number:
        chain_length += 1
        sum += chain_length
    print("Chain length ", chain_length)

    for L in range(1, chain_length):
        a = (number - L * (L+1) / 2) / (L+1)
        if a == int(a):
            count += 1
    return count

numbers = [5, 9, 15]


# print(find_consecutive_sum(numbers[2]))
# print(find_consecutive_sum1(numbers[2]))
print(find_consecutive_sum2(numbers[2]))












