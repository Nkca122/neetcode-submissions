# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root, M=float("-inf")):
    if not root:
        return 0
    if root.val >= M:
        print(f"{root.val} {root.left} {root.right}")
        return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
    if not root.left and not root.right:
        if root.val >= M:
            print(root.val)
            return 1
        else:
            return 0
    return dfs(root.left, M) + dfs(root.right, M)

    

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return dfs(root)
        