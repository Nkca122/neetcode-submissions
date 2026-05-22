# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            node = curr
            for _ in range(n):
                node = node.next
            if not node:
                break
            else:
                prev = curr; curr = curr.next
            
        if curr:
            if not prev:
                head = head.next
            else:
                prev.next = curr.next
        return head
            
            
        