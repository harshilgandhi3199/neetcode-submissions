class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [6, 1, 2, 3, 4, 5]
        # if nums[mid] > nums[right] -> find in right space
        # else find in left space
        left = 0
        right = len(nums) - 1

        while left < right:
            # early return if current window is already sorted
            if nums[left] <= nums[right]:
                return nums[left]

            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
