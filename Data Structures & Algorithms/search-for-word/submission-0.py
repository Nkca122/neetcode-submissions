class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def solve(index, i, j):
            # Base Case: If we matched all characters, we found the word!
            if index == len(word):
                return True
                
            # Boundary check and character mismatch check
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[index]:
                return False
            
            # 1. Mark the current cell as visited
            temp = board[i][j]
            board[i][j] = "#"
            
            # 2. Explore all 4 directions
            # If ANY direction returns True, we can stop and return True
            found = (
                solve(index + 1, i - 1, j) or # Up
                solve(index + 1, i + 1, j) or # Down
                solve(index + 1, i, j - 1) or # Left
                solve(index + 1, i, j + 1)    # Right
            )
            
            # 3. Backtrack: Restore the original character for other paths
            board[i][j] = temp
            
            return found

        # Kick off the search from every cell that matches the first letter
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if solve(0, i, j): # Start index at 0 to let 'solve' handle validation
                        return True
                        
        return False