class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for mask in range(pow(2, len(nums))):
            curr = []
            for i in range(len(nums)):
                bit = mask & 1
                if bit:
                    curr.append(nums[i])
                mask >>= 1
            result.add(tuple(sorted(curr)))
        return [list(res) for res in result] 