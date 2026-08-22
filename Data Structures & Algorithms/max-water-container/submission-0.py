class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0

        max_area = 0
        left_ptr, right_ptr = 0, n - 1

        while left_ptr <= right_ptr:
            left_bar = height[left_ptr]
            right_bar = height[right_ptr]
            
            max_area = max(max_area, min(left_bar, right_bar) * (right_ptr - left_ptr))

            if left_bar < right_bar: left_ptr += 1
            elif right_bar < left_bar: right_ptr -=1
            else:
                left_ptr += 1
                right_ptr -= 1


        return max_area
