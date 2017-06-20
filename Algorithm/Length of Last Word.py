# Time O(n)
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        i = len(s)-1
        endSpaces = 0
        
        while i >=0 and s[i] == ' ':
                endSpaces += 1
                i -= 1
                
        i = len(s)-1 - endSpaces
        
        while i >= 0 and s[i] != ' ':
            i -= 1
            
        return len(s)-endSpaces-i-1
        
# Another pythonic method
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])
