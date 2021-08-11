# Brute Force -- O(n^2) time | O(1) space

def twoSum(array, targetSum):
	for i in range(len(array) - 1):
		first_num = array[i]
		for j in range(i + 1, len(array)):
			second_num = array[j]
			if first_num + second_num == targetSum:
				return [first_num, second_num]
	return []