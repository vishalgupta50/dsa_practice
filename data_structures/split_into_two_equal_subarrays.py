"""
Given an array of integers greater than zero, find if it is possible to split it in two subarrays (without reordering the elements),
such that the sum of the two subarrays is the same. Print the two subarrays.

Examples :

Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
Output :  { 1 2 3 4 }
          { 5 , 5 }

Input : Arr[] = { 4, 1, 2, 3 }
Output : {4 1}
         {2 3}

Input : Arr[] = { 4, 3, 2, 1}
Output : Not Possible

"""


def split_two_equal_subarrays(ilist):
    end = len(ilist) - 1
    start = 0
    end_sum, start_sum = ilist[end], ilist[start]

    while end >= start:
        if start_sum < end_sum:
            start += 1
            start_sum += ilist[start]
        else:
            end -= 1
            end_sum += ilist[end]

        if start_sum == end_sum:
            print(ilist[:start+1])
            print(ilist[end:])
            return ilist[:start+1], ilist[end:]



ilist1 = [4, 3, 2, 1]
ilist2 = [1, 2, 3, 4, 5, 5]
ilist3 = [4, 1, 2, 3]

print(split_two_equal_subarrays(ilist2))
