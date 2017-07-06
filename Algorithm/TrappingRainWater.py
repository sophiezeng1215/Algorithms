# Time O(n), Space O(n)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftHigh = [0]
        for i in range(1, len(height)):
            leftHigh.append(max(height[i-1],leftHigh[i-1]))
        rightHigh = 0
        water = 0
        for i in range(len(height)-2, -1, -1):
            rightHigh = max(rightHigh, height[i+1])
            wall = min(rightHigh, leftHigh[i])
            if height[i] < wall:
                water += wall - height[i]
        return water 
            
