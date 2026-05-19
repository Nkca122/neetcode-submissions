class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) > 1:
            s = "".join([ch.lower() if ch.isalnum() else "" for ch in s])
            l = 0; r = len(s) - 1
            while l <= r:
                print(s[l], s[r])                
                if s[l] != s[r]:
                    return False
                l += 1; r -= 1
        return True
        