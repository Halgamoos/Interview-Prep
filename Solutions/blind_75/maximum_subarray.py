# https://leetcode.com/problems/maximum-subarray/

# O(n) time | O(1) space
class Solution:
    def maxSubArray(self, nums):
        max_sub = nums[0]
        curr_sum = 0
        
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sub = max(max_sub, curr_sum)
        return max_sub
    
