"""The problem asks for all unique triplets whose sum is zero.
A brute-force approach would take O(n³), so we optimize using sorting and the two-pointer technique.

First, we sort the array so duplicates are grouped and pointer movement becomes predictable.
Then, we fix one element using a for loop. For the remaining part of the array, we use two pointers—one starting just after the fixed element and one at the end.

Depending on the sum, we move the pointers inward. If the sum is zero, we store the triplet, move both pointers, and skip duplicates to avoid repeating the same triplet.

We also skip duplicate fixed values to ensure uniqueness.

The overall time complexity is O(n²), which is optimal for this problem."""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums)-1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0 :
                   res.append([nums[i], nums[left], nums[right]])
                   left += 1 
                   right -=1 
                   while left < right and nums[left] == nums[left - 1]:
                        left += 1
                   while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0 :
                    left += 1
                else:
                    right -=1
        
        return res        
      