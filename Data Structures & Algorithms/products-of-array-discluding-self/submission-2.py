class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        zero_cnt = 0
        output = [0] * n
        
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                prod *= num

        if zero_cnt > 1:
            return output

        if zero_cnt == 1:
            for i in range(n):
                if nums[i] == 0:
                    output[i] = prod
        else:
            for i in range(n):
                output[i] = int(prod / nums[i])

        return output
