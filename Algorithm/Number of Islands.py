# https://segmentfault.com/a/1190000003753307
#我们每找到一个1，就将其标为0，这样就能把整个岛屿变成0
# Time O(M*N), Space O(max(M, N))

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfsFillZeros(grid, i, j)
        return res
        
    def dfsFillZeros(self, grid, i, j):
        grid[i][j] = '0'
        if j>0 and grid[i][j-1] == '1':
            self.dfsFillZeros(grid, i, j-1)
        if i > 0 and grid[i-1][j]== '1':
            self.dfsFillZeros(grid, i-1, j)
        if j < len(grid[i])-1 and grid[i][j+1] == '1':
            self.dfsFillZeros(grid, i, j+1)
        if i < len(grid)-1 and grid[i+1][j] == '1':
            self.dfsFillZeros(grid, i+1, j)
