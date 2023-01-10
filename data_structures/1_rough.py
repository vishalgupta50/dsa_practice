stri = "abcd sdf sdfs"
print(stri[1])

print(ord('a') - 96)

# for i in stri:
#     print(i)


x = [3, 4, 89, 21]
print(x, id(x))

y = list(x)
print(y, id(y))
y[3] = 32

x.sort()
print(x, id(x))

print(y, id(y))



str1 = "abcd "
print(str1, id(str1))

str2 = str1.rstrip()
print(str2, id(str2))
print(str1, id(str1))


x = [67, 23, 90, 2, 1, 45]
print(x, id(x))
x.sort()
# sorted(x)
print(x, id(x))

y = [89, 45, 90, 67, 23, 88]
print(y, id(y))
z = sorted(y)
print(z, id(z))




bal_dict = {
    "[": 1,
    "{": 2
}
print(bal_dict)

char = "("
bal_dict[char] = 5

print(bal_dict)


for key, value in bal_dict.items():
    print(key, value)

y = [89, 45, 90, 67, 23, 88]
print(y)
print(y.pop(0))
print(y)
print(id(y))
y.sort()
print(id(y))
















































































































































































#