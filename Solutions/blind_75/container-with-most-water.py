# https://leetcode.com/problems/container-with-most-water/

# Brute force (Time Limit Exceeded)
# O(n^2) time | O(1) space
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = right - left
                min_length = min(height[left], height[right])
                
                curr_area = width * min_length
                max_area = max(curr_area, max_area)
        return max_area

# Two Pointers
# O(n) time | O(1) space
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            min_length = min(height[right], height[left])
            width = right - left
            
            curr_area = min_length * width
            max_area = max(max_area, curr_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area