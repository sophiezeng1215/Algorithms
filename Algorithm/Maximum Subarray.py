# O(n), space O(1)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        local_max = global_max = nums[0]
        for i in range(1, len(nums)):
            local_max = max(nums[i], local_max + nums[i])
            global_max = max(local_max, global_max)
        return global_max
