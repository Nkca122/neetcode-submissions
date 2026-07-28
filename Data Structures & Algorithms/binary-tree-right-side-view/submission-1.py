# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Do a level order traversal and choose the rightmost element
        if not root:
            return []
        
        q = deque([root])
        res = []

        while q:
            level = []
            for i in range(len(q)):
                front = q.popleft()

                if front.left is not None:
                    q.append(front.left)
                if front.right is not None:
                    q.append(front.right)
                
                level.append(front.val)
            res.append(level[-1])
        return res