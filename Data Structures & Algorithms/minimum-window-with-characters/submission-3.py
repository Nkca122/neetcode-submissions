def freq(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
def comparator(s, t):
    freqS = freq(s); freqT = freq(t)
    for key in freqT:
        if freqT[key] > freqS.get(key, 0):
            return False
    return True
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s); nt = len(t)
        if nt > ns:
            return ""
        l = 0; r = l + nt - 1; curr = None
        while l <= r and r < ns:
            if comparator(s[l : r + 1], t):
                while comparator(s[l : r + 1], t):
                    l += 1
                curr = s[l - 1 : r + 1] if curr is None or len(curr) > r - l + 2 else curr
            else:
                r += 1
        return curr if curr is not None else ""


        