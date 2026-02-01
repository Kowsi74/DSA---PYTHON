"""_The problem: Move Zeros 

Approach :  
    * I used two pointer approach 
    * Fast scans the entire element in the array
    * Slow keep track of where the next non-zero goes
    * If there is any non-zero i safely overwrite it,
      it moves all non-zero value to front in position
    * After first while loop slow points to the indeces where the zero should start
    * i replace all remaining value with zero
    
Time and Space Complexity:
    --Time complexity is 0(n) because i traverse at most twice
    --Space complexity is 0(1) in place i used only two variables

    """


def moveZeroes(nums):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != 0 :
            nums[slow] = nums[fast]
            slow += 1
        fast += 1 
    while slow < len(nums):
        nums[slow] = 0
        slow += 1