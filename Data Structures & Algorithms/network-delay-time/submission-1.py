from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for ui, vi, ti in times:
            adj_list[ui].append((ti, vi))
        
        # Initially
        visited = [False] * (n + 1)
        dist = [float("inf")] * (n + 1)
        stack = []

        # Visiting source node
        visited[k] = True
        dist[k] = 0
        stack.append((0, k))

        while stack:
            d, u = stack.pop()
            for ti, vi in adj_list[u]:
                if d + ti < dist[vi]:
                    dist[vi] = d + ti
                    stack.append((d + ti, vi))
        ans = max(dist[1:])
        return ans if ans < float("inf") else -1
