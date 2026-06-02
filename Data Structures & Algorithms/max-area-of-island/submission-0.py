class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                def solve(i, j):
                    if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])) or grid[i][j] != 1:
                        return 0
                    grid[i][j] = -1 # Exhausted Land
                    land = solve(i + 1, j) + solve(i - 1, j) + solve(i, j - 1) + solve(i, j + 1) + 1
                    return land
                if grid[i][j] == 1:
                    max_area = max(solve(i, j), max_area)
        return max_area
        