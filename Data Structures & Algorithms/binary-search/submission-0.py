class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0; e = len(nums) - 1
        while s <= e:
            mid = (s+e)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    e -= 1
                else:
                    s += 1
        return -1
        