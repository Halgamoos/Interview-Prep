# https://leetcode.com/problems/reverse-linked-list/

# Iterative approach using 3 pointers
# O(n) time | O(1) space
class Solution:
    def reverseList(self, head):
        prev_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next # Remember next node
            curr_node.next = prev_node  # REVERSE! None, first time round.
            prev_node = curr_node  # Used in the next iteration.
            curr_node = next_node  # Move to next node.
        head = prev_node
        return head