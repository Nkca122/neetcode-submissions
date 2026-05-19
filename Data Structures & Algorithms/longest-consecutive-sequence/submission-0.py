class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = defaultdict(int); res = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num in freq:
            # Taking a starting point
            if num - 1 not in freq:
                curr_res = 0
                while num in freq:
                    curr_res += 1; num += 1
                res = max(res, curr_res)
        return res

        