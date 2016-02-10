#!/usr/bin/python
# 1, 2, 3
from sets import Set
def subsets(S):
    """
    1. Corner Case
    2. Difference between append and concatenate

    Time Complexity: O(n^2)
    Space depth of stack
    """
    if S == None:
        return None
    if S == []:
        return [[]]
    curr = subsets(S[1:])
    for ele in curr[:]:
        new = sorted([S[0]] + ele)
        if new not in curr:
	    curr.append(new)

    return curr

test = [4, 4, 4, 1, 4]
print subsets(test) 
