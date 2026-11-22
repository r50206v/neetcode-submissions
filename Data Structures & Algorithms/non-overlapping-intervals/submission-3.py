class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prev_end = intervals[0][1]
        rm_count = 0

        for start, end in intervals[1:]:
            if prev_end > start:
                prev_end = min(prev_end, end)
                rm_count += 1
            else:
                prev_end = end
        return rm_count
# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         if not intervals:
#             return 0

#         intervals.sort(key=lambda x: x[0])
#         ans = intervals[0]
#         rm_count = 0

#         for intv in intervals[1:]:
#             if ans[1] > intv[0]:
#                 ans = (
#                     ans[0], 
#                     min(intv[1], ans[1])
#                 )
#                 rm_count += 1
#             else:
#                 ans = intv
#         return rm_count

