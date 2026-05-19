class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        hash_list = sorted(list(hash.items()), key = lambda x : x[1], reverse=True)
        res = []
        for item in hash_list[:k]:
            res.append(item[0])
        return res
        

        
            


        