#!/usr/bin/python

def permuteKao(nums):
    """
    no return value for insert and append, + has reture value
    notice range(len(perm) + 1)
    """
    if len(nums) == 0:
        return [[]]

    perms = permuteKao(nums[1:])
    first = nums[0]
    ret = []
    print "perms: " + str(perms)
    for perm in perms[:]:
        for i in range(len(perm) + 1):
            ret.append(perm[:i] + [first] + perm[i:])

    return ret


def permute(nums):
    """
    DO NOT forget to check None!
    """
    if nums is None:
        return []
    if nums == []:
        return [[]]
        
    curr = permute(nums[1:])
    ret = []
    for elem in curr:
        for i in range(len(elem) + 1):
            ret.append(elem[:i] + [nums[0]] + elem[i:])
    
    return ret

test = [1, 2, 2]

print permute(test)
