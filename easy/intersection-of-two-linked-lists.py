class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        
        ptrA = headA
        ptrB = headB
        
        while ptrA is not ptrB:
            ptrA = headB if ptrA is None else ptrA.next
            ptrB = headA if ptrB is None else ptrB.next
            
        return ptrA