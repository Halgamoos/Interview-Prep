# https://leetcode.com/problems/one-edit-distance/

# O(n) time | O(1) space
class Solution(object):
    def isOneEditDistance(self, s, t):
        ns, nt = len(s), len(t)

        # both input strings can't be the same
        if s == t:
            return False

        # Ensure that s is shorter than t.
        if ns > nt:
            return self.isOneEditDistance(t, s)

        # The strings are NOT one edit away distance  
        # if the length diff is more than 1.
        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                # if strings have the same length
                if ns == nt:
                    return s[i + 1:] == t[i + 1:]
                # if strings have different lengths
                else:
                    return s[i:] == t[i + 1:]
        
        return True