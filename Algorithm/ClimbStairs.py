
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
        prev1 = 1
        prev2 = 1
        total = 0
        for i in range(2,n+1):
            total = prev1 + prev2
            prev2 = prev1
            prev1 = total
        return total
