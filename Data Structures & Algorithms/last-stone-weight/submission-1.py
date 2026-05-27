import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            print(stones)
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if x == y:
                continue
            else:
                leftover = -1 * abs(x - y)
                heapq.heappush(stones, leftover)
        return -1 * stones[0] if stones else 0
