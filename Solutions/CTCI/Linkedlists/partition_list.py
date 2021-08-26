# https://leetcode.com/problems/partition-list/

# O(n) time | O(1) space
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # two pointers:
            # less_than pointer --> less_than --> 1 --> 2 --> 2  
            # greater_equal pointer --> great_eq --> 4 --> 3 --> 5 
            # point end of less_than to great_eq.next
            # less_than pointer to None at the tail
        
        less_head = less_ptr = ListNode(0)
        great_eq_head = great_eq_ptr = ListNode(0)
        
        while head:
            if head.val < x:
                less_ptr.next = head
                less_ptr = less_ptr.next
            else:
                great_eq_ptr.next = head
                great_eq_ptr = great_eq_ptr.next
            
            head = head.next
        
        # now we have two linked lists as shown above
        great_eq_ptr.next = None
        less_ptr.next = great_eq_head.next
        
        return less_head.next

# CTCI Example in and out:
# Input - 5 -> 6 -> 3 -> 5 -> 4 -> 10 -> None, key = 4
# Output - 3 -> 5 -> 6 -> 5 -> 4 -> 10 -> None