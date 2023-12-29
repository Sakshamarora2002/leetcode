# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m=0
        current=head
        while current:
            m+=1
            current=current.next
        if n>m or n<=0:
            return head
        prev=None
        current=head
        target_index=m-n
        while target_index>0:
            prev=current
            current=current.next
            target_index-=1
        if prev:
            prev.next=current.next
        else:
            head=current.next
        return head





        