#!/usr/bin/python

def permutePIEHelper(nums, visited, ret, curr, index):
    if index == len(nums):
        ret.append(curr[:])
        return
    
    # not from range(index, len(nums))
    for i in range(0, len(nums)):
        if visited[i] == 1 or \
           (i > 0 and visited[i - 1] and nums[i] == nums[i - 1]):
            continue
        else:
            visited[i] = 1
            curr.append(nums[i])
            permutePIEHelper(nums, visited, ret, curr, index + 1)
            curr.pop()
            visited[i] = 0
        


def permutePIE(nums):
    """
    PIE: P95
    If no duplicated, make sure you SORTED the list first!
    """
    if nums is None:
        return []
    ret = []
    curr = []
    visited = [0] * len(nums)
    permutePIEHelper(sorted(nums), visited, ret, curr, 0)
    return ret

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

test = [3,3,0,3]

print permutePIE(test)
