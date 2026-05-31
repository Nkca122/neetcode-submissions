class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            c_pos = abs(abs(nums[i]) - 1)
            if nums[c_pos] < 0:
                return abs(nums[i])
            nums[c_pos] *= -1
        return -1
