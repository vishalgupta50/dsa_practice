# Input: list1 = [10, 20, 4]
# Output: 10
#
# Input: list2 = [70, 11, 20, 4, 100]
# Output: 70

list1 = [10, 20, 4, 45, 99]
# list1 = [10, 10, 10, 10]


# Method 1
# Sorting is easier but less optimal method

"""
# 3 scenarios
# mx = list1[0]
secondmax = list1[1]

we will traverse
i = 2 to n i in range(2,n)
case 1: if list1[i] > mx
    secondmax = mx
    mx = list1[i]
case 2: if list1[i] > secondmax & list1[i] != mx
    secondmax = list1[i]
case 3: mx == secondmax & secondmax != list1[i]
    secondmax = list1[i] 
"""

mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)

for i in range(2,n):
    if list1[i] > mx:
        print("1")
        secondmax = mx
        mx = list1[i]
        print("1 end")
    elif list1[i] > secondmax & list1[i] != mx:
        print("2")
        secondmax = list1[i]
        print("2 end")
    elif mx == secondmax & secondmax != list1[i]:
        print("3")
        secondmax = list1[i]
        print("3 end")

print(secondmax)



# Method 2
"""
1. sort the element in ascending or descending order and fetch the secnond largest number, expensive process
2. removing duplicates is required here
"""
list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]

list2 = list(set(list1))
list2.sort()
print(list2)
print("second largest ", list2[-2])



employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

def get_age(employee1):
    return employee1.get('age')

print(get_age(employees[1]))

employees.sort(key=get_age)
print(employees)

employees.sort(key=lambda x: x.get('age'))

print(employees)


list1 = [[10, 20], [20, 4, 45, 45, 45], [99, 99, 0], [3, 5,6,4,6,7]]
list1.sort(key=len)
print(list1)




