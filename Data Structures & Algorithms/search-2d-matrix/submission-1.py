class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix); columns = len(matrix[0])
        r = 0; s = 0; e = columns - 1
        while r < rows and matrix[r][e] < target:
            r += 1
        if r >= rows:
            return False
        
        while s <= e:
            mid = (s + e)//2
            if matrix[r][mid] == target:
                return True
            else:
                if matrix[r][mid] > target:
                    e -= 1
                else:
                    s += 1
        return False
        
        

        