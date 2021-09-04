# https://leetcode.com/problems/product-of-array-except-self/

# Two Pass
# O(n) time | O(1) time


def productExceptSelf(nums):
    result = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    return result

test = [
    [[1, 2 , 3 , 4], [24, 12, 8, 6]],
    [[1, 2 , 3 , 4], [24, 12, 8, 6]],
    [[1, 2 , 3 , 4], [24, 12, 8, 6]]
]

for input_array, correct_result in test:
    my_result = productExceptSelf(input_array)
    print(input_array, correct_result, my_result, my_result == correct_result, sep = " | ")