

#11. Container With Most Water
#Result: Accepted   652 ms  24 MB
class Solution(object):
    def maxArea(self, height):
        #Solution for O(n) time 
        maxarea = 0 
        l = 0
        r = len(height) - 1
        while l < r:
            maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
            if (height[l] < height[r]):
                l = l + 1
            else:
                r = r - 1
        return maxarea
        
# Solution for O(n^2), not intersting 
# class Solution(object):
#     def maxArea(self, height):
# 		maxValue = 0
# 		for i in range(0, len(height) - 1):
# 			for j in range(i+1, len(height)):
# 				current = min(height[i], height[j]) * (j-i)
# 				maxValue = current if current >= maxValue else maxValue
# 		return maxValue