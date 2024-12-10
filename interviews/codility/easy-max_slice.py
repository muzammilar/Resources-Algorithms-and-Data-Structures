# max slice: max consecutive sum.
# simply add all sums, and the max slice would be the difference between the sum ending at that pace

def max_slice(A)
    max_slice = max_ending = 0
    for x in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)