class Solution:
    # find greater boundary l and r for each index, then calculate water trapped at that 
    # index using this formula: min(height[l], height[r]) - height[i]
    def trap(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            left = height[i]
            right = height[i]
            l, r = i, i
            while l >= 0:
                left = max(height[l], left)
                l -= 1
            while r < len(height):
                right = max(height[r], right)
                r += 1
            max_area += min(left, right) - height[i]

        return max_area
