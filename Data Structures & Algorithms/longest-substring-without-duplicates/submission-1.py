def unique(s : str) -> bool:
    return len(set(s)) == len(s)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        st = 0; e = st + 1; maxL = 1;
        while st < e and e < n:
            if unique(s[st : e + 1]):
                maxL = max(maxL, e - st + 1); e += 1
            else:
                st += 1; e += 1
        return maxL




            
        