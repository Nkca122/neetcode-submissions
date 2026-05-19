class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows & Columns
        for i in range(9):
            hashR = {}; hashC = {}
            for j in range(9):
                R = board[i][j]; C = board[j][i]
                
                # Row
                if R != ".":
                    hashR[R] = hashR.get(R, 0) + 1
                    if hashR[R] > 1:
                        return False
                
                # Column
                if C != ".":
                    hashC[C] = hashC.get(C, 0) + 1
                    if hashC[C] > 1:
                        return False
        
        # Sub matrices
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                hash = {}
                for r in range(3):
                    for c in range(3):
                        if board[i+r][j+c] != ".":
                            hash[board[i+r][j+c]] = hash.get(board[i+r][j+c], 0) + 1
                            if hash[board[i+r][j+c]] > 1:
                                return False
        return True




        