# https://leetcode.com/problems/valid-anagram/

# Takeaway: Hashtables can be used for clever solutions like this one

class Solution(object):
    def isAnagram(self, s, t):
        # if s and t have same # of occurences of each char, return True

        counter = {}
            
        if len(s) != len(t):
            return False
        
        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
        
        for char in t:
            if char in counter:
                counter[char] -= 1
            else:
                return False
            
        for val in counter.values():
            if val != 0:
                return False
        
        return True