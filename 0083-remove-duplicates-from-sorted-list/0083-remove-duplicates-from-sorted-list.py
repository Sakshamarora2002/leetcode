class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = ListNode()  # Dummy node for the new linked list
        new_tail = new_head

        temp = head
        while temp and temp.next:
            if temp.val != temp.next.val:
                new_tail.next = temp
                new_tail = new_tail.next
            temp = temp.next

        # Handle the last element if it is also a duplicate
        new_tail.next = temp

        return new_head.next
