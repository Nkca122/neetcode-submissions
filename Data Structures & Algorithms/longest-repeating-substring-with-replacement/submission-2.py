def mode(s : str) -> int:
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return max(freq.values())
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n <= 1:
            return n
        l = 0; r = l + 1; maxL = 1
        while l < r and r < n:
            if (r - l + 1) - mode(s[l:r+1]) <= k:
                maxL = max(maxL, r - l + 1); r += 1
            else:
                l += 1; r += 1
        return maxL
            
            

        