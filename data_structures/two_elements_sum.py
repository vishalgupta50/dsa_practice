arr = [5, 7, 10, 3, 6, 2, 9, 10]
sum_no = 12
oarr = []


for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == sum_no:
            oarr.append([arr[i], arr[j]])

print(oarr)


hasharr = dict()

for i in range(len(arr)):
    complement = sum_no - arr[i]
    if complement in hasharr:
        print(complement, arr[i])
    else:
        hasharr[arr[i]] = arr[i]






