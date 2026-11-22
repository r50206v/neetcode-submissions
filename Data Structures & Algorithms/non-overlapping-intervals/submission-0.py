class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = [intervals[0]]

        for intv in intervals[1:]:
            if ans[-1][1] > intv[0]:
                ans[-1] = (
                    ans[-1][0], 
                    min(intv[1], ans[-1][1])
                )
            else:
                ans.append(intv)
        return len(intervals) - len(ans)

