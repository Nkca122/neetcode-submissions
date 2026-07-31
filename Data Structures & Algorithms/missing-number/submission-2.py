class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        mask = 0
        for i in range(1, n + 1):
            mask = mask ^ i
        
        for num in nums:
            mask = mask ^ num
        
        return mask