from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sub = defaultdict(list)
        for s in strs:
            sub["".join(sorted(s))].append(s)
        
        return list(sub.values())
