def validate_palindrome(number):
    new_temp = 0
    number1 = number
    while number > 0:
        temp = number % 10
        new_temp = new_temp * 10 + temp
        number = number // 10
    if number1 == new_temp:
        return True
    else:
        return False


print(validate_palindrome(121))




print(121//10)