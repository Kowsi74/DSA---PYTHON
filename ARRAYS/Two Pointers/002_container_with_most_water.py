""" The problem asks us to find two vertical lines such that the container formed between them stores the maximum water.
A brute-force approach would be to check all pairs using nested loops, which takes O(n²) time, so it’s inefficient.
To optimize this, I use a two-pointer approach — one pointer at the start and one at the end.
The area depends on the minimum height and the distance between the pointers.
Since the area is limited by the smaller height, moving the taller pointer will not increase the area, so we move the pointer with the smaller height.
This way, we traverse the array once with O(n) time and O(1) space. """


def maxArea(self, height: List[int]) -> int:
        max_area = 0 
        left = 0 
        right = len(height)-1
         
        while left < right:
            h = min(height[left],height[right])
            w = right - left
            current_area = h * w 
            if current_area > max_area:
                max_area= current_area
            
            if height[left] < height[right]:
                left += 1 
            else:
                right -=1 
        return max_area


