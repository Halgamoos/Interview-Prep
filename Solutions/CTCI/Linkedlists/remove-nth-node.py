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

# Approach #2: Use slow, fast, and dummy pointers
# O(n) time | O(1) space
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy
        
        for _ in range(n):
            if fast != None:
                fast = fast.next
            else: 
                return None
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy.next

