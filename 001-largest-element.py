"""
Problem:
Find the largest element in an array

Approach:
- Start with first element as maximum
- Traverse the array
- Update maximum when a larger element is found

Time Complexity: O(n)
Space Complexity: O(1)

"""


def largest_element(nums):
    if len(nums) == 0:
        return None

    current_max = nums[0]
    for num in nums:
        if num > current_max:
            current_max = num

    return current_max
print(largest_element([1,10,14,7,0]))
