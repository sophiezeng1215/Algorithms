# use a div to get the left digit and /10 to get the right digit
# x = (x%div)/10

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        while div <= x/10:   # e.g., x = 3, div = 1; x = 30, div = 10
            div *= 10
        while x > 0:
            if x/div != x%10:
                return False
            x = (x%div)/10
            div /= 100
        return True
