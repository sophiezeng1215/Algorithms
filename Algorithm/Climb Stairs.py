
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 0:
            return 0
        p1 = 1
        p2 = 1
        res = 0
        for i in range(2,n+1):
            res = p1 + p2
            p2 = p1
            p1 = res
        return res
