#!/usr/bin/python
# Original implementation used too many
# isBadVersions() function call
# simplify the solution here:

A = [False] * 9 + [True]
print (A)
def isBadVersion(index):
    return A[index-1]

def findFirstBadVersion(n):
    # write your code here
    start = 0
    end = n        
    if n == 1 and isBadVersion(1) == True:
        return 1
        
    while end >= start:
        mid = (start + end)/2
        if isBadVersion(mid) == True:
            end = mid - 1 
        else:
            start = mid + 1

    if isBadVersion(start) == True:
        return start
    else:
        return end
    
print 'the bad version is', findFirstBadVersion(10)
