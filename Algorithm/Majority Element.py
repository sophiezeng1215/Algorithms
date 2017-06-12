# Time O(n), space O(1)
# use a "cummulative count". Once count <= 0, the current num is the assigned maj. Use a second loop to check whether the maj is real or not. 

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = None
        count = 0
        for i in range(len(nums)):
            if nums[i] == maj:
                count +=1
            else:
                count -= 1
                if count <= 0:
                    count = 1
                    maj = nums[i]
        count = 0
        for num in nums:
            if num == maj:
                count += 1
        if count > len(nums)/2:
            return maj
        else:
            return None
