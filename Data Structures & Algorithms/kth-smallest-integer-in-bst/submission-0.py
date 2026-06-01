# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []; q = [root]
        while q:
            front = q.pop(0)
            if front:
                heapq.heappush(heap, front.val)
                q.append(front.left)
                q.append(front.right)
        for _ in range(k-1):
            heapq.heappop(heap)
        return heap[0]
