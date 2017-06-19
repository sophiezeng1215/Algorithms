# Time O(n), space O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        maxLength = 0
        visited = set()
        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            length = right - left + 1
            maxLength = max(maxLength, length)
        return maxLength
            
