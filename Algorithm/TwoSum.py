# O(n), space O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in nums_dict:
                return [nums_dict[rem], i]
            nums_dict.update({nums[i]: i})
        return None
    
 # after sorting, another way


