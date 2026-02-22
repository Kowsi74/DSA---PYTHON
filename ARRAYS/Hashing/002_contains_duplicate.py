"""this is the brute force approach which takes o(n) in time o(1) in space
it works with nested loop one loop for one loop is moving and 
another one is scan entire array 
if the value is same its return true else return false"""

def containsduplicates(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

""" now it is the time to optimize the code using hash map
    one approach is using dictionary and count the frequency 
    if the count is more than 1 duplicate exists so we return true
    else false it takes o(n) in time and o(n) in space but think 
    one thing there frequency really need ? Noo bcaz they dont care 
    about count they only asking true or false like if exists
    or not thats it
"""

def containsduplicate(nums):
    seen = {}
    for num in nums:
        if num in seen :
            seen[num] += 1
        else:
            seen[num] = 1
        if seen[num] > 1:
            return True
    return False

""" Another approach is using set creating a set and
    iterate throgh the array if the value is already exists
    return true else add on that value in set and if not exists
    return False it will take o(n) in time and o(n) space
"""
def containsduplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

"""And there is also a one line solution for this question which is 
    okay but always explain and understand it also took o(n) in time 
    because we using set(nums) so it iterates n times thats why 
    and o(n) in space
"""

def containsduplicate(nums):
    if len(nums) != len(set(nums)):
        return True
    return False 
    