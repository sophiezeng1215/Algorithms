# Time O(n), space O(1)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {')':"(", '}':'{',']':'['}
        for char in s:
            if char in pairs and stack:
                if stack.pop()!= pairs[char]:
                    return False
            elif char in pairs:
                return False
            else:
                stack.append(char)
        return len(stack) == 0
