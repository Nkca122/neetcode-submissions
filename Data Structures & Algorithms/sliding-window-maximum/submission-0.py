class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0; r = l + k; res = []
        while l < r and r <= len(nums):
            res.append(max(nums[l:r]))
            l += 1; r = l + k
        return res

        