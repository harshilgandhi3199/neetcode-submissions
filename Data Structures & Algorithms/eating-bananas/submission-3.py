class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def timeTaken(rate):
            time = 0
            for i in range(len(piles)):
                time += (piles[i] + (rate - 1)) // rate
            
            return time

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if timeTaken(mid) > h:
                left = mid + 1
            else:
                right = mid

        return right