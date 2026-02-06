"""The problem is to return a sorted array of squares from a sorted input array. 
    Squaring breaks the order because negative values can produce larger squares.
    So I use a two-pointer approach: one pointer at the start and one at the end.
    At each step, I compare absolute values, square the larger one, and place it at the end of the result array, moving the corresponding pointer.
    This continues until all elements are processed. 
    The time complexity is O(n) and space complexity is O(n)
    we can't do it with o(1) bcaz output order is reversed and we need extra array"""
    
def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1
        pos = n - 1   # fill result from end

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result[pos] = nums[right] * nums[right]
                right -= 1
            else:
                result[pos] = nums[left] * nums[left]
                left += 1
            pos -= 1

        return result
