# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root1, root2):
            nonlocal res

            if not root1 and not root2:
                return 
            
            if not root1 or not root2:
                res = False; return
            
            if root1.val != root2.val:
                res = False
            
            dfs(root1.left, root2.left)
            dfs(root1.right, root2.right)

        dfs(p, q)
        return res
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        def dfs(r, s):
            nonlocal res

            if not r or not s:
                return
            
            if r.val == s.val:
                if self.isSameTree(r.left, s.left) and self.isSameTree(r.right, s.right):
                    res = True; return

            dfs(r.left, s)
            dfs(r.right, s)
        
        dfs(root, subRoot)
        return res
            