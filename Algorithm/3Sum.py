# Time O(nlgn + n2) = O(n2). Space O(solution)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-1,-1,-1):     # start from the end
            if i==len(nums)-1 or nums[i] != nums[i+1]:   # to avoid duplication
            subsets = self.twoSum(nums[:i], -nums[i])
            for subset in subsets:
                    subset.append(nums[i])
                    res.append(subset)
        return res
                
    def twoSum(self, nums, target):   # list all pairs, different from LC twosum
        i = 0
        j = len(nums)-1
        res = []
        while i<j:
            if nums[i]+nums[j] == target:
                res.append([nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i]==nums[i-1]:   
                    i += 1
                while j > i and nums[j]==nums[j+1]:
                    j -= 1
            elif nums[i] + nums[j] < target:
                i += 1;
            else:
                j -= 1
        return res
