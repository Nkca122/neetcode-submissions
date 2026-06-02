class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                def solve(i, j):
                    if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])) or grid[i][j] != "1":
                        return False
                    grid[i][j] = "#" # Discovered land
                    land = (
                        solve(i + 1, j) or
                        solve(i - 1, j) or
                        solve(i, j - 1) or
                        solve(i, j + 1)
                    )
                    return land
                if grid[i][j] == "1":
                    solve(i, j); res += 1
        return res