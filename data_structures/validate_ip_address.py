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
    new_s = s.split(".")
    for elem in new_s:
        if int(elem) in range(0, 255) and len(elem) < 4:
            flag = 0
        else:
            flag = 1
        if flag == 1:
            return 0
    return 1




validIP = "222.111.111.111"
validIP1 = "0000.0000.0000.0000"
invalidIP = "456.333.2.1"

print(isValidIP(validIP))
print(len("222"))
print("222".isdigit())
# print(validIP.split("."))
# print(list(1:10))


