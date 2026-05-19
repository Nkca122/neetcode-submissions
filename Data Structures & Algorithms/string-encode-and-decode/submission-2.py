class Solution:
    def encode(self, strs: List[str]) -> str:
        return "\t".join(strs) + "\n" * len(strs)

    def decode(self, s: str) -> List[str]:
        res = []; curr = ""
        for ch in s:
            if ch != "\t" and ch != "\n":
                curr += ch
            elif ch == "\t":
                res.append(curr); curr = ""
            elif ch == "\n":
                res.append(curr); break
        return res
            
