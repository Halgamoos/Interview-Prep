# https://leetcode.com/problems/rotate-string/

# 
# O(n^2) time | O(n) space
class Solution_2:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)

# O(n^2) time | O(1) space
class Solution_1:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return True
        
		# Copy the original string to know when we've rotated back to the origin
        original_A = A

        while A:
            # Each iteration rotates A one character to the right
            A = A[-1:] + A[:-1]
            if A == B:
                return True
            if A == original_A:
                return False


test_s = 'abcde'
test_goal = 'cdeab' # return True