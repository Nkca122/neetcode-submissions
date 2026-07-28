# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            level = []
            for i in range(len(q)):
                front = q.popleft()

                # Add children
                if front.left is not None:
                    q.append(front.left)
                if front.right is not None:
                    q.append(front.right)

                level.append(front.val)
            res.append(level.copy())
        return res

                