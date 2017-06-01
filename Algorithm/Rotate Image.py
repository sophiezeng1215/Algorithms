#time complexity O(size of the matrix), space complexity O(1)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-1-i):
                temp = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-1-i][n-j-1]
                matrix[n-1-i][n-j-1] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = temp
