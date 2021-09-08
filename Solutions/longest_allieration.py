# https://binarysearch.com/problems/Longest-Alliteration

class Solution:
    def solve(self, words):
        maxcnt, cnt = 0, 1
        prev_char = ""
        for word in words:
            if prev_char == "":
                prev_char = word[0]
            elif prev_char == word[0]:
                cnt += 1
            else:
                prev_char = word[0]
                cnt = 1
            maxcnt = max(maxcnt, cnt)
        return maxcnt