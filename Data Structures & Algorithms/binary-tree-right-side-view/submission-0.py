# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]; result = []
        while queue:
            # rightmost node on the level
            print([n.val for n in queue], result)
            result.append(queue[-1].val)
            
            # adding the next level to the queue
            n = len(queue)
            for i in range(n):
                node = queue[i]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            queue = queue[n:]
        return result



        