"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h1 = head; h2 = None; correspondences = []
        while h1:
            new_node = Node(x = h1.val)
            if not h2:
                h2 = new_node
            else:
                temp = h2
                while temp.next:
                    temp = temp.next
                temp.next = new_node
            correspondences.append((h1, new_node))
            h1 = h1.next
        
        # Assigning randoms
        
        for node1, node2 in correspondences:
            if node1.random:
                h1 = head; h2_dash = h2
                while h1 != node1.random:
                    h1 = h1.next; h2_dash = h2_dash.next
                node2.random = h2_dash
        return h2



        