# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, M = float("-inf")):
            nonlocal res
            if not root:
                return
            
            if root.val >= M:
                res += 1
                M = root.val
            
            dfs(root.left, M)
            dfs(root.right, M)
        
        dfs(root)
        return res
            