def letter_range(digit):
    s = (digit - 2) * 3
    offset = 0 if digit != 8 and digit != 9 else 1
    r = 3 if digit != 7 and digit != 9 else 4

    result = []
    for i in range(r):
        result.append(chr(ord('a') + s + offset + i))
    return result

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        result = []
        def solve(index, curr):
            if index >= len(digits):
                result.append(curr); return
            digit = int(digits[index])
            for letter in letter_range(digit):
                solve(index + 1, f"{curr}{letter}")
    
        solve(0, "")
        return result