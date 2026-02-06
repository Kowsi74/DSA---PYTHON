"""The problem is to remove duplicates from a sorted array, allowing at most two occurrences.
    Brute-force nested loops are O(n²), so we optimize using a two-pointer approach. 
    The slow pointer tracks the next position to write a valid element and moves only when including it, while fast scans every element.
    We include nums[fast] if it is different from nums[slow-2], ensuring at most two duplicates.
    The first two elements are always valid. Time complexity is O(n) and space complexity is O(1)"""
    

def removeDuplicates(self, nums: List[int]) -> int:
    slow = 2
    fast = 2
    while fast < len(nums):
        if slow < 2 or nums[fast] != nums[slow-2]:
            nums[slow]=nums[fast]
            slow += 1
            fast += 1
    return slow
