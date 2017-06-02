# O(n), space O(1)

class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        self.reverseSublist(s, 0, len(s)-1)
        i = 0
        for j in range(len(s)):
            if s[j] == ' ':
                self.reverseSublist(s, i, j-1)
                i = j + 1
        self.reverseSublist(s, i, len(s)-1)
        
    def reverseSublist(self, s, start, end):
        while start < end:
            temp = s[end]
            s[end] = s[start]
            s[start] = temp
            start += 1
            end -= 1
