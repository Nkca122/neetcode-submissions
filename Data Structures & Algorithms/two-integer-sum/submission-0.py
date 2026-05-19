class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            numsj = target - nums[i]
            if hash.get(numsj, None) is not None:
                res = [i, hash.get(numsj, None)]; res.sort()
                return res
            hash[nums[i]] = hash.get(nums[i], i)
        return []

        