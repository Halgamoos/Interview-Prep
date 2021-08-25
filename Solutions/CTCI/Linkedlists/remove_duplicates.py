# if linkedlist is sorted
# O(n) time | O(1) space
class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head

# if linkedlist is NOT sorted --> we use set() 
#                             --> I think we can also use hash table
# O(n) time | O(n) space
def removeDuplicates(head):
    if head is None:
        return head

    items = set()
    items.add(head.val)
    curr = head

    while curr and curr.next:
        if curr.next.val in items:
            curr.next = curr.next.next
        else:
            items.add(curr.next.val)
            curr = curr.next
    return head
