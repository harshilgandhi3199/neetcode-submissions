import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # start with k = max(piles), because h >= len(piles) so in order to 
        # eat all bananas within h hours, we will atleast need k rate.
        left = 1
        right = max(piles)

        # lower k as long as hours <= h; else return k
        while left < right:
            mid = (left + right) // 2
            total_hours = sum(math.ceil(p / mid) for p in piles)
            if total_hours <= h:
                right = mid
            else:
                left = mid + 1

        return right
        