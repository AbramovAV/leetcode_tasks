class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ptr = head
        while ptr is not None and ptr.next is not None:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        if head and head.val == val: head = head.next
        return head