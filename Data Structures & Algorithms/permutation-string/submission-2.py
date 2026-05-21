def permutation(s1, s2):
    return "".join(sorted(s1)) == "".join(sorted(s2))
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1); n2 = len(s2)
        if n2 < n1:
            return False
        l = 0; r = l + n1 - 1
        while l <= r and r < n2:
            if permutation(s2[l:r+1], s1):
                return True
            else:
                l += 1; r += 1
        return False

        