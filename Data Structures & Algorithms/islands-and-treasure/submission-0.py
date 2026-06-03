class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    def solve(i, j, dist):
                        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == -1 or (grid[i][j] == 0 and dist > 0):
                            return 
                        
                        if dist > grid[i][j]:
                            return
                        
                        grid[i][j] = dist
                        dist += 1
                        return (
                            solve(i + 1, j, dist) or 
                            solve(i - 1, j, dist) or
                            solve(i, j + 1, dist) or
                            solve(i, j - 1, dist)
                        )
                    solve(i, j, 0)
            
                    
