"""The problem asks to reverse a string in-place, meaning I am not allowed to use extra space.

I use a two-pointer approach. I place the left pointer at the beginning of the list and the right pointer at the end.

While left < right, I swap the characters at these two positions. This puts the correct character in both ends simultaneously.

After swapping, I move left one step to the right and right one step to the left.

The loop stops when the pointers meet or cross, because at that point all characters are already reversed.

Each character is swapped once, so the time complexity is O(n).
No extra space is used, so the space complexity is O(1)."""


def reverseString(self, s: List[str]) -> None:
        left = 0 
        right = len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -=1 
        return s