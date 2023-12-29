# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        mergedlist=dummy
        while list1 and list2:
            if list1.val<=list2.val:
                mergedlist.next=list1
                list1=list1.next
            else:
                mergedlist.next=list2
                list2=list2.next
            mergedlist=mergedlist.next
        if list1:
            mergedlist.next=list1
        if list2:
            mergedlist.next=list2
        return dummy.next