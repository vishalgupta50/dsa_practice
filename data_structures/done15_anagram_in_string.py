"""
"anagram in string"
check wheather two string are anagram
"""

string1 = "silentl"
string2 = "listens"


def check_anagram(str1, str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1 == str2:
        return True
    else:
        return False


def check_anagram1(str1, str2):
    str1_dict = {}
    for char in str1:
        if char in str1_dict:
            str1_dict[char] += 1
        else:
            str1_dict[char] = 1

    for char in str2:
        if char in str1_dict:
            str1_dict[char] -= 1
        else:
            return False

    for value in str1_dict.values():
        if value != 0:
            return False

    return True


import pytest


@pytest.fixture()
def setup_resources():
    print("before")
    yield
    print("after")


def test_check_anagram():
    assert check_anagram1("hello", "ellho") == True

# print(check_anagram(string1, string2))
# print(check_anagram1(string1, string2))
