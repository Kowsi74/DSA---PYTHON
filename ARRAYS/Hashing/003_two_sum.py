"""
    for this problem they asking if the sum of two values in the array
    is equal to the target return the index of that two values
    so frst the brute force approach is using nested loops and 
    iterate through the loops and checking but it takes o(n^2) in time and o(1) in space
"""
def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target :
                return [i,j]
    
    
"""
    next approach is sorting first and using two pointer but  sorting before always
    think about original indices where they was ask output as original indices
    so we create one list inside we create one tuple to safe the original indices and after we 
    areget using two pointers and the output it n times we iterate creating list takes o(n) and sort takes o(n log n )
    and two pointer takes o(n) so overall it takes o(n log n) in time and o(n) in space 
"""       
def twosum(nums,target):
    arr = [(num , i) for i , num in enumerate(nums)]
    arr.sort()
    left = 0 
    right = len(arr)-1
    while left < right:
        current_sum = arr[left][0] + arr[right][0]
        if current_sum == target:
            return [arr[left][1],arr[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1  
            
"""
    the final appraoch is using hash map which is optimal one 
    in this i create one dictionary and using enumerate to manage the original indices
    iterate through array and calculating diff of target with value 
    if the diff is already in dict it will return the current index and the dict(index)
    it will take o(n) in time and o(n) in space 
"""            

def two_sum(nums,target):
    seen = {}
    for i , num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return[seen[diff], i]
        seen[num] = i
        
    
