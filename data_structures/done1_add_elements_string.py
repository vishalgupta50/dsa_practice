"""
IP: 421
OP: 491
Explanation : 4+2+1+42+21+421
IP: 123
OP: 164
Explanation : 1+2+3+12+23+123

IN:1234
OP:1670
1+2+3+4+12+23+34+123+234+1234

IP and OP are in string format.
"""

"""
[4, 2, 1, 42, 21, 421]





"""


# input_number = "421"
input_number = "1234"

def add_elements_of_number(input_str):

    sum = 0
    new_list = []
    for i in range(len(input_str)):
        for j in range(i + 1, len(input_str) + 1):
            sum = sum + int(input_str[i:j])
            new_list.append(input_str[i:j])
    print(new_list)
    return sum




def add_elements_of_number1(input_str):

    try:
        input_len = len(input_str)
        list1 = []
        if input_len < 0:
            return "Bad parameter"
        else:
            temp_number = int("1" + (input_len) * "0")
            input_str = int(input_str)

        print(temp_number)
        sum = 0
        while temp_number > 0:
            # list1.append(input_str % temp_number)
            num = input_str % temp_number
            list1.append(num)

            if temp_number == 10 and len(str(input_str)) > 1:
                input_str = input_str // 10
                input_len = len(str(input_str))
                temp_number = int("1" + input_len * "0")
            else:
                temp_number = temp_number // 10

            sum += num


            print(temp_number)
            print(list1)
            print(sum)

    except Exception as err:
        print(str(err))



    return []





# print(add_elements_of_number(input_number))
print(add_elements_of_number1(input_number))




