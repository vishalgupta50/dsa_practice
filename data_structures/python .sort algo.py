# TimSort is a sorting algorithm based on Insertion Sort and Merge Sort.
#
# Used in Java’s Arrays.sort() as well as Python’s sorted() and sort().
# First sort small pieces using Insertion Sort, then merges the pieces using a merge of merge sort.

MIN_MERGE = 32

def calcMinRun(n):
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.

    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1

    print("4. ", n + r)
    return n + r


arr = [-2, 7, 15, -14, 0, 15, 0,
           7, -7, -4, -13, 5, 8, -14, 12]

n = len(arr)
calcMinRun(n)

print("1. len n = {} ", n)


print("2.", n >= MIN_MERGE)
r = 0
r |= n & 1
print("3. ", r)

x = 0
x = x | n & 1
print("5. ", x)


and1 = n & 1
print("6. ", and1)
or1 = 0
or1 = or1 | and1
print("7. ", or1)






