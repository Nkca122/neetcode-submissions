class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        l = 0; r = len(matrix[0]); t = 0; b = len(matrix)
        zeroes = []
        for i in range(b):
            for j in range(r):
                if matrix[i][j] == 0:
                   zeroes.append((i, j))
        print(zeroes)
        for row, col in zeroes:
            for j in range(r):
                matrix[row][j] = 0
            for i in range(b):
                matrix[i][col] = 0
            

        