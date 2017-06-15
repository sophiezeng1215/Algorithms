# Time O(n), Space O(n)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        leftHigh = [0]
        for i in range(1, len(height)):
            leftHigh.append(max(leftHigh[i-1], height[i-1]))
        rightHigh = 0
        for i in range(len(height)-2, -1, -1):
            rightHigh = max(rightHigh, height[i+1])
            if min(leftHigh[i], rightHigh) > height[i]:
                water += (min(leftHigh[i], rightHigh) - height[i])
        return water
