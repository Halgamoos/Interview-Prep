#  https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Approach #1: 
    # loop through LL and find length
    # delete the node at (length - n + 1)
# O(n) time | O(1) space
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # [dummy -> 1 -> 2 -> 3 -> 4 -> None], n = 2          
        dummy = ListNode(0)
        dummy.next = head
        
        length = 0
        first = head
        while first != None:
            length += 1
            first = first.next
        
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        
        first.next = first.next.next
        
        return dummy.next

