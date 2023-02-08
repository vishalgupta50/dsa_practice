"""
[1, 3, 6, 2, 3, 2, 4, 7, 8]

n = 3
grp1 = [1, 2, 3]
grp2 = [2, 3, 4]
grp3 = [6, 7, 8]

"""

def group(ilist, n):
    grps = []

    for i in range(n):
        num1 = ilist[i] + 1
        num2 = ilist[i] + 2
        if num1 in ilist and num2 in ilist:
        # if num1 and num2 in ilist:
            if [ilist[i], num1, num2] not in grps:
                grps.append([ilist[i], num1, num2])

    print(grps)


    return grps



ilist = [1, 3, 6, 2, 3, 2, 4, 7, 8]
n = len(ilist)
print(n)
group(ilist, n)













