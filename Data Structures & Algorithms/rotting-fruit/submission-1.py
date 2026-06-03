class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rotten = deque([])
        t = 0
        freshCt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    freshCt += 1
        
        while rotten and freshCt > 0:
            t += 1
            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    new_i, new_j = i + dx, j + dy
                    if new_i >= len(grid) or new_i < 0 or new_j >= len(grid[0]) or new_j < 0:
                        continue
                    if grid[new_i][new_j] == 0 or \
                    grid[new_i][new_j] == 2:
                        continue

                    grid[new_i][new_j] = 2
                    rotten.append((new_i, new_j))
                    freshCt -= 1
        if freshCt > 0:
            return -1
        return t
    
