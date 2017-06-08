# Time O(n) Space O(1)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        key = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[key+1] = nums[i]
                key += 1
        for i in range(key+1, len(nums)):
            nums[i] = 0
  
