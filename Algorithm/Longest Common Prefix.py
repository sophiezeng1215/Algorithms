# Time O(n), space O(1)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i in range(len(strs[0])):
            for string in strs:
                if i >= len(string) or string[i] != strs[0][i]:
                    if i == 0:
                        return ''
                    else:
                        return strs[0][:i]
        return strs[0]



# using a sameflag
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sameFlag = True
        res = ''
        if len(strs) == 0:
            return ""
        i = 0
        while i < range(len(strs[0])) and sameFlag:
            for string in strs:
                if i >= len(string) or string[i] != strs[0][i]:
                    sameFlag = False
                    break
            if sameFlag:
                res = res + strs[0][i]
            i += 1
        return res
                
