"""The problem asks for all unique triplets whose sum is zero.

I first sort the array, which helps me use the two-pointer technique and handle duplicates easily.

I fix one element using a loop, and for the remaining part of the array, I use two pointers to find pairs that sum to the negative of the fixed value.

If the sum is too small, I move the left pointer to increase it; if the sum is too large, I move the right pointer to decrease it.

I skip duplicate values for the fixed element and also for the left and right pointers to avoid repeated triplets.

This approach runs in O(n²) time and uses O(1) extra space."""

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
      