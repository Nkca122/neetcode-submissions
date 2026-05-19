class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        if len(nums) > 1:
            for i in range(len(nums)):
                hash[nums[i]] = hash.get(nums[i], 0)
                if hash[nums[i]] > 0:
                    return True
                hash[nums[i]] += 1
        return False
        