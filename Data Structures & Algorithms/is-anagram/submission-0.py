class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s = "".join(sorted(s)); t = "".join(sorted(t))
            return s == t
        return False
        