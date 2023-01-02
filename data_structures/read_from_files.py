
with open("../python_concepts/file1.txt") as file:
    data = file.read()

print(data)

from collections import Counter

res = Counter(data)

print(dict(res))
print(type(res))
print(res['e'])


# without counter
dict1 = {}

for char in data:
    # print("1 ", char)
    # count = 0
    if char.isalpha():
        # print("2 ", char)
        # print(type(char))
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1


print("dict1")
print(dict1)
print(type(dict1))



# print(data)






from typing import Dict


char_dict = {}
# type: Dict[str, int]


def char_count(string: str) -> dict:
    new_string = string.lower()
    for c in new_string:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict


# if __name__ == "__main__":
UserString = "Enter Input String: "
CharCount = char_count(UserString)
print("Characters Count: ", CharCount)






