# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None; ptr1 = list1; ptr2 = list2
        while ptr1 and ptr2:
            new_node = ListNode()
            if ptr1.val < ptr2.val:
                new_node.val = ptr1.val; ptr1 = ptr1.next
            else:
                new_node.val = ptr2.val; ptr2 = ptr2.next
            
            if res:
                temp = res
                while temp.next:
                    temp = temp.next
                temp.next = new_node
            else:
                res = new_node
        
        if ptr1:
            if res:
                temp = res
                while temp.next:
                    temp = temp.next
                temp.next = ptr1
            else:
                res = ptr1
        
        if ptr2:
            if res:
                temp = res
                while temp.next:
                    temp = temp.next
                temp.next = ptr2
            else:
                res = ptr2
        
        return res
            


                        