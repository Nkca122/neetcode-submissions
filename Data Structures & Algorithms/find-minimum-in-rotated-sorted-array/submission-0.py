class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) < 2:
            return nums[0]
        s = 0; e = n-1
        while nums[s] > nums[e]:
            s += 1
        return nums[s]
        