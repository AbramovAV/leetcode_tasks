class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = {}
        while head:
            if head.next not in seen_nodes:
                seen_nodes[head] = head.next
            else:
                return True
            head = head.next
        return False