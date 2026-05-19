class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for s in strs:
            key = "".join(sorted(s)); hash[key] = hash.get(key, [])
            hash[key].append(s)
        return list(hash.values())
            



        