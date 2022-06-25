class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = merged_list = ListNode(0)
      
        while list1 and list2:
            if list1.val<list2.val:
                merged_list.next = list1
                list1 = list1.next
            else:
                merged_list.next = list2
                list2 = list2.next
            merged_list = merged_list.next
        
        merged_list.next = list1 or list2
        return head.next