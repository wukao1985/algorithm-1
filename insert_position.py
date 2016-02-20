#!/usr/bin/python

def searchInsert(A, target):
    """
    Q: 1) is it sorted? 
       2) Does the array have dup elements?
    Corner Case:
       When A is an empty array
    """
    # write your code here
    if A == []: return 0
    return helper(A, target, 0, len(A) - 1)
    
def helper(A, target, st, end):
    if A[st] >= target:
        return st
    if A[end] == target:
        return end
    if A[end] < target:
        return end + 1
 
    middle = (st + end) / 2
    if target == A[middle]:
        return middle
    elif target < A[middle]:
        return helper(A, target, st, middle - 1)
    else:
        return helper(A, target, middle + 1, end)


# [1, 3, 5, 6] insert 2 return 1
# [], 9
print searchInsert([1, 3, 5, 6], 2)
