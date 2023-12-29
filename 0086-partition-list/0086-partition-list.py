# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesshead = lesstail = ListNode(0)
        greaterhead = greatertail = ListNode(0)
    
        while head:
            if head.val < x:
                lesstail.next = head
                lesstail = lesstail.next
            else:
                greatertail.next = head
                greatertail = greatertail.next
            head = head.next
    
        greatertail.next = None
        lesstail.next = greaterhead.next
    
        return lesshead.next