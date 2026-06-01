class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []; subset = []
        def solve(idx):
            if idx >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[idx])
            solve(idx + 1)
            subset.pop()
            solve(idx + 1)
        solve(0)
        return result