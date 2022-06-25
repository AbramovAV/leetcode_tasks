class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = None
        while head is not None:
            prev_ptr = head
            head = head.next
            prev_ptr.next = ptr
            ptr = prev_ptr
        return ptr