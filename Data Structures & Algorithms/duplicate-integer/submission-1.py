from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = defaultdict(bool)
        for num in nums:
            if arr[num]:
                return True
            arr[num] = True
        return False
