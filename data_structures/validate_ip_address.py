"""
nput:
IPv4 address = 222.111.111.111
Output: 1
Explanation: Here, the IPv4 address is as
per the criteria mentioned and also all
four decimal numbers lies in the mentioned
range.

Example 2:

Input:
IPv4 address = 5555..555
Output: 0
Explanation: 5555..555 is not a valid
IPv4 address, as the middle two portions
are missing.
Y
"""

print(int("22"))

def isValidIP(s):
    parts = s.split(".")
    if len(parts) > 4:
        return False
    for part in parts:
        # if int(part) in range(0, 255) and len(part) < 4:
        if not part.isdigit() or int(part) > 255 or (len(part) > 0 and part.startswith('0')):
            return False
    return True




validIP = "222.111.111.111"
validIP1 = "0000.0000.0000.0000"
validIP2 = "456.333.2.1"

print(isValidIP(validIP))
# print(len("222"))
# print("222".isdigit())
# print(validIP.split("."))
# print(list(1:10))


regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


"""
validate ipv6 address and uncompress it also
"""



lst = [56, 5, 12, 1, 23, 56, 10, 78, 45, 78]

def second_largeest(lst):
    first = max(lst[0], lst[1])
    second = min(lst[0], lst[1])

    if len(lst) <= 0:
        return False

    for i in range(2, len(lst)):
        if lst[i] > first:
            second = first
            first = lst[i]
        elif second < lst[i] < first:
            second = lst[i]
        # elif

    return second


print(second_largeest(lst))



num = 40

def print_binary(num):
    binary = 0
    while num > 0:
        temp = num % 2
        binary = binary + temp * 10
        num = num // 2
    return binary


print(print_binary(num))











