class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}

        for i in range(len(nums)):
            key = target - nums[i]
            if key in num:
                return sorted([i, num.get(key, -1)])
            num[nums[i]] = i

        return []