"""The problem asks us to find two indices in a sorted array such that their sum equals the target, and return the indices in 1-based format.

Initially, I made the mistake of overchecking the sum and not fully trusting the two-pointer approach.

A brute-force solution would be to use two nested loops and check every pair, which takes O(n²) time. This is not optimal.

Since the array is sorted, we can optimize using the two-pointer technique. I place one pointer at the start and one at the end.

On each iteration, I compute the current sum. If it equals the target, I return the indices. If the sum is greater than the target, I move the right pointer left to reduce the sum. If the sum is smaller, I move the left pointer right to increase the sum.

This works because the array is sorted and pointer movement predictably changes the sum.

The time complexity is O(n) since each pointer moves at most n times, and the space complexity is O(1).

The problem guarantees one solution, so we return as soon as we find it."""



def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        if len(numbers) < 2: 
            return 
        while left < right :
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1 , right + 1]
            elif current_sum > target :
               right -=1
            elif current_sum < target :
               left += 1 
               
               

        
    
