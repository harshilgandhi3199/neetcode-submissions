class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        longestSeq = 1
        curr_len = 1

        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) > 1:
                longestSeq = max(longestSeq, curr_len)
                curr_len = 1
            elif abs(nums[i] - nums[i - 1]) == 0:
                continue
            else:
                curr_len += 1

        return max(longestSeq, curr_len)
