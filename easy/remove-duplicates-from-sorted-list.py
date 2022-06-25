class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
                continue
            ptr = ptr.next
        return head