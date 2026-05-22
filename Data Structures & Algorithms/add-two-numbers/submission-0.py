# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1; temp2 = l2; global total; global carry; res = []; total = 0; carry = 0
        while temp1 or temp2:
            total = (temp1.val if temp1 else 0) + (temp2.val if temp2 else 0) + carry
            carry = total // 10
            total = total % 10

            temp1 = temp1.next if temp1 else None
            temp2 = temp2.next if temp2 else None

            res.append(total)
        if carry > 0:
            res.append(carry)

        hr = None
    
        for digit in res:
            new_node = ListNode(digit)
            if hr is None:
                hr = new_node
            else:
                temp = hr
                while temp.next:
                    temp = temp.next
                temp.next = new_node
        
        return hr

         
                
        