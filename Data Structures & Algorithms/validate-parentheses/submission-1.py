class Solution:
    def isValid(self, s: str) -> bool:
        stack = []; brackets = {
            "(" : 1, ")" : -1,
            "{" : 2, "}" : -2,
            "[" : 3, "]" : -3
        }

        for bracket in s:
            if brackets[bracket] > 0:
                stack.append(bracket)
            else:
                if stack:
                    if brackets[stack[-1]] + brackets[bracket] != 0:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        return True if not stack else False
        