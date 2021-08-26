# https://leetcode.com/problems/palindrome-linked-list/

# Approach 1: Use an array to store values
# O(n) time | O(n) Space
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        arr = []
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        
        return arr == arr[::-1]

