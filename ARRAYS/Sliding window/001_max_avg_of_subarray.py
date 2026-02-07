"""The problem asks for the maximum average among all subarrays of length k.

A brute-force solution using nested loops would compute the sum of every subarray and take O(n²) time, which is inefficient.

Since the subarray length k is fixed, I use a fixed-size sliding window approach.

First, I calculate the sum of the first k elements and store it as the initial maximum sum.
Then, I slide the window one position at a time by subtracting the element leaving the window and adding the new element entering the window.

At each step, I compare the current window sum with the maximum sum and update it if needed.

After processing all windows, I divide the maximum sum by k to get the maximum average.

This solution runs in O(n) time and uses O(1) extra space."""

def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0 
        for i in range(k):
            window_sum += nums[i]
        max_sum = window_sum
        for i in range(k,len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum , window_sum)

        return max_sum/k
            

