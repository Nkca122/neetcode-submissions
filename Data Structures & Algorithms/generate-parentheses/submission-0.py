class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def solve(curr, weight):
            print(curr)
            if len(curr) >= 2*n:
                if weight == 0:
                    res.append(curr)
                return
            curr = curr + "("
            solve(curr, weight + 1)
            
            if weight > 0:
                curr = curr[:-1]
                solve(f"{curr})", weight - 1)
        solve("", 0)
        return res