class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        def solve(idx):
            if sum(subset) > target:
                return
            if idx >= len(nums):
                if sum(subset) == target:
                    result.append(subset.copy())
                return
            # with num
            subset.append(nums[idx])
            # repeated num
            solve(idx)

            # remove num and move to the next index
            subset.pop()
            solve(idx + 1)
        solve(0)
        return result