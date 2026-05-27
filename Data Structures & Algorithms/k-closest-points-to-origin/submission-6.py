def calculate_distance(x, y):
    return (pow(x, 2) + pow(y, 2)) ** 0.5

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for xi, yi in points:
            if len(res) < k:
                heapq.heappush(res, (-1 * calculate_distance(xi, yi), (xi, yi)))
            else:
                if -1 * calculate_distance(xi, yi) > res[0][0]:
                    heapq.heappop(res); heapq.heappush(res, (-1 * calculate_distance(xi, yi), (xi, yi)))
        output = [t[1] for t in res]
        return output
        