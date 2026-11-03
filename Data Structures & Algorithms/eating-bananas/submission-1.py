class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        left, right = 1, max(piles)
        while left <= right:
            mid = (right + left) // 2
            taken_hours = sum([math.ceil(float(p) / mid) for p in piles])

            if taken_hours > h:
                left = mid + 1
            elif taken_hours <= h:
                right = mid - 1
            
        return left