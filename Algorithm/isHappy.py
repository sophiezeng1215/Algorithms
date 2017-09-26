class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in seen:
                return False
            else: 
                seen.add(n)
        return True

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        present = set()
        while n != 1:
            div = 1
            while n/div >= 10:
                div = div * 10
            newnum = 0
            while div > 0:
                newnum = newnum + (n/div)**2
                n = n % div
                div = div/10
            if newnum == 1:
                return True
            elif newnum in present:
                return False
            else:
                present.add(newnum)
                n = newnum
        return True
        
        
