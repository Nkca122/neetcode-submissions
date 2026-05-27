import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.ans = []; self.k = k
        for i in range(len(nums)):
            if len(self.ans) >= k:
                if self.ans[0] < nums[i]:
                    heapq.heappop(self.ans); heapq.heappush(self.ans, nums[i])
            else:
                heapq.heappush(self.ans, nums[i])


    def add(self, val: int) -> int:
        if not self.ans:
            heapq.heappush(self.ans, val); return val
        else:
            if len(self.ans) >= self.k:
                if self.ans[0] < val:
                    heapq.heappop(self.ans); heapq.heappush(self.ans, val)
            else:
                heapq.heappush(self.ans, val)
            return self.ans[0]
        
