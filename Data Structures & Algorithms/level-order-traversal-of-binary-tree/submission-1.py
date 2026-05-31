# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]; result = []; level = 0
        while queue:
            for node in queue:
                if node:
                    if len(result) < level + 1:
                        result.append([])
                    result[level].append(node.val)
            
            level += 1
            n = len(queue)

            for i in range(n):
                if queue[i]:
                    queue.append(queue[i].left)
                    queue.append(queue[i].right)
            queue = queue[n:]
        return result


        