class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ct = 0
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    def bfs(x, y):
                        nonlocal r, c
                        q = [(x, y)]
                        grid[x][y] = "X"
                        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                        while q:
                            x, y = q.pop(0)
                            for dx, dy in delta:
                                if 0 <= x + dx < r and 0 <= y + dy < c and grid[x + dx][y + dy] == "1":
                                    q.append((x + dx, y + dy)); grid[x + dx][y + dy] = "X"
                    bfs(i, j); ct += 1
        return ct

