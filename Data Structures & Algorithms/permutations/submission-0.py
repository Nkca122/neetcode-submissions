class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = set()
        def solve(available, curr, target):
            print(curr)
            if len(curr) >= target:
                result.add(tuple(curr))
            for i in range(len(available)):
                curr.append(available[i])
                solve([*available[0:i], * available[i+1:]], curr, target)
                curr.pop()

        solve(nums, [], len(nums))
        return [list(res) for res in result]