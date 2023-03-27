"""
Find Duplicate characters in a string

"""

string = "I am hello world and python is my language"


def find_duplicate_chars(string):
    duplicates = dict()

    for i in range(len(string)):
        if string[i] in duplicates:
            duplicates[string[i]] += 1
        else:
            duplicates[string[i]] = 1

    for key, value in duplicates.items():
        if value > 1 and key != " ":
            print(key, value)

    return duplicates


if __name__ == "__main__":
    string = "I am hello world and python is my language"
    find_duplicate_chars(string)

















