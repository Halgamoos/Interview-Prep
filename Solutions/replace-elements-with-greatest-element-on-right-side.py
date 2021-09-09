# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
                         -1  --> new_max
        [17, 18, 5, 4, 6, 1] 
                          i  
        """
        right_max = -1 
        for i in range(len(arr) -1, -1 , -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max
        return arr