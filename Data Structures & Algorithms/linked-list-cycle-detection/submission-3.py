# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        while s and f:
            if s:
                s = s.next
            if f:
                if f.next:
                    f = f.next.next
                else:
                    f = f.next
                
            if s == f and f is not None:
                return True
        return False
        