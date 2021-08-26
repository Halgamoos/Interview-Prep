# https://leetcode.com/problems/delete-node-in-a-linked-list/

# O(1) time | O(1) space
class Solution:
    def deleteNode(self, node):
        # make curr node val equal to the next node val
        node.val = node.next.val
        # 'delete' the next node
        node.next = node.next.next