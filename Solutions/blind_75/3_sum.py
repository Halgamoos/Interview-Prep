# https://leetcode.com/problems/3sum/

# O(n^2) time | O(n) space --> i think...
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        # i = index, a = "int element" in nums
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                # continue to next iteration of loop
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result