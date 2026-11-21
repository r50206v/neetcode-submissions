from bisect import bisect_left, bisect_right

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval

        # first interval whose end >= s  (the first one that could overlap)
        lo = bisect_left(intervals, s, key=lambda x: x[1])
        # first interval whose start > e (the first one that definitely doesn't overlap)
        hi = bisect_right(intervals, e, key=lambda x: x[0])

        # intervals[lo:hi] all overlap newInterval, so fold them in
        if lo < hi:
            s = min(s, intervals[lo][0])
            e = max(e, intervals[hi - 1][1])

        intervals[lo:hi] = [[s, e]]
        return intervals