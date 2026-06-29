class Solution:
    # To find the amount of water trapped at index i,
    # we need the hightest walls on both sides and then
    # we use the previous formula to find the amount of water.
    # But we also know that the water trapped is defined by
    # the minimum height of the 2 boundaries
    # This means we don't need to find the exact height of the walls
    # on both sides. If we knew that there exisit a wall higher than
    # current wall to the left or right, but since the amount
    # of water trapped is determined by the height of smaller
    # wall we have enough information to calculate the amount
    # of water at this index
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        # keep track of heighest bars each ptr has seen
        leftMax, rightMax = height[left], height[right]
        area = 0

        while left < right:
            # leftMax is the heighest wall to the left of left + 1
            if leftMax < rightMax:
                left += 1
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    area += leftMax - height[left]
            else:
                right -= 1
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    area += rightMax - height[right]

        return area