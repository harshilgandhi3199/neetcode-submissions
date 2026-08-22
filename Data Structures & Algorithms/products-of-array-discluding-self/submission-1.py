class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        totalProduct = 0
        zeros = []
        output = [0] * n
        
        for i in range(n):
            if nums[i] == 0:
                zeros.append(i)

        if len(zeros) > 1:
            totalProduct = 0
            return output
        else:
            for i in range(n):
                if nums[i] != 0 and totalProduct == 0:
                    totalProduct += nums[i]
                elif nums[i] == 0:
                    zeros.append(i)
                else:
                    totalProduct *= nums[i]

        if len(zeros) > 0:
            while len(zeros) > 0:
                idx = zeros.pop()
                output[idx] = totalProduct
        else:
            for i in range(n):
                if nums[i] == 0:
                    output[i] = totalProduct
                    continue

                output[i] = int(totalProduct / nums[i])

        return output
