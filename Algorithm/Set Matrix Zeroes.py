# Use the first row and column to mark zero positions
# O(m * n)

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        firstRowZero = False
        firstColumnZero = False
        
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                firstRowZero = True
                break
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                firstColumnZero = True
                break
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if firstRowZero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        if firstColumnZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
