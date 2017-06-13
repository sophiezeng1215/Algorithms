# Time O(n), Space O(1)
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000 }
        num = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                num = num - roman[s[i]]
            else:
                num = num + roman[s[i]]
        return num + roman[s[-1]]