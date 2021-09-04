# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# binary search
# O(log n) time | O(1) space
class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_result = nums[0]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # in a sorted array, left most index is always the minimum amount
            if nums[left] <= nums[right]:
                min_result = min(min_result, nums[left])
                break
            
            mid = (left + right) // 2
            min_result = min(min_result, nums[mid])
            
            if nums[mid] >= nums[left]:
                # search right
                left = mid + 1
            else:
                # search left
                right = mid - 1
        return min_result