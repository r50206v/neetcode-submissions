class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        ans = intervals[0]
        rm_count = 0

        for intv in intervals[1:]:
            if ans[1] > intv[0]:
                ans = (
                    ans[0], 
                    min(intv[1], ans[1])
                )
                rm_count += 1
            else:
                ans = intv
        return rm_count

