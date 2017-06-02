# O(n), space O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        key = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[key]:
                key += 1
                nums[key] = nums[i]
        return key + 1
